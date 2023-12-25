# rental/management/commands/populate_dummy_data.py

from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from rental.models import Car, Customer, Booking, Review
from faker import Faker
import random

fake = Faker()

class Command(BaseCommand):
    help = 'Populate the database with dummy data'

    def handle(self, *args, **options):
        # Create dummy users
        users = []
        for _ in range(100):
            user = User.objects.create_user(
                username=fake.user_name(),
                email=fake.email(),
                password='password'
            )
            users.append(user)

        # Create dummy cars
        cars = []
        for _ in range(100):
            car = Car.objects.create(
                name=fake.word(),
                model=fake.word(),
                status=fake.word(),
                seat=random.randint(2, 6),
                door=random.randint(2, 4),
                gearbox=random.choice(['M', 'A']),
                price=random.uniform(50, 200)
            )
            cars.append(car)

        # Create dummy customers
        customers = []
        for user in users:
            customer = Customer.objects.create(
                phone_number=fake.phone_number(),
                user=user
            )
            customers.append(customer)

        # Create dummy bookings with conflict checking
        for _ in range(100):
            start_date = fake.date_between(start_date='-30d', end_date='today')
            end_date = fake.date_between(start_date='today', end_date='+30d')
            car = random.choice(cars)
            customer = random.choice(customers)

            # Check for conflicts before creating a booking
            if not Booking.objects.filter(
                car=car,
                end_date__gte=start_date,
                start_date__lte=end_date
            ).exists():
                Booking.objects.create(
                    start_date=start_date,
                    end_date=end_date,
                    customer=customer,
                    car=car
                )

        # Create dummy reviews
        for car in cars:
            Review.objects.create(
                car=car,
                name=fake.name(),
                description=fake.text(),
            )

        self.stdout.write(self.style.SUCCESS('Dummy data populated successfully.'))
