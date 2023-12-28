import random
from django.core.management.base import BaseCommand
from faker import Faker
from django.contrib.auth.models import User
from rental.models import Car

fake = Faker()

class Command(BaseCommand):
    help = 'Populate User and Car tables with dummy data'

    def handle(self, *args, **kwargs):
        self.populate_users(100)
        self.populate_cars(100)
        self.stdout.write(self.style.SUCCESS('Data populated successfully!'))

    def populate_users(self, count):
        for _ in range(count):
            username = fake.user_name()
            email = fake.email()
            password = fake.password()

            # Ensure unique usernames
            while User.objects.filter(username=username).exists():
                username = fake.user_name()

            User.objects.create_user(username=username, email=email, password=password)

    def populate_cars(self, count):
        for _ in range(count):
            name = fake.word()
            model = fake.word()
            available = random.choice([True, False])
            seat = random.randint(2, 8)
            door = random.randint(2, 5)
            gearbox = random.choice(['M', 'A'])
            price = round(random.uniform(20, 200), 2)

            car = Car.objects.create(
                name=name,
                model=model,
                availabile=available,
                seat=seat,
                door=door,
                gearbox=gearbox,
                price=price
            )