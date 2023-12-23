from django.shortcuts import get_object_or_404, render

# Create your views here.
# views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.views import View
from django.utils.decorators import method_decorator
from django.utils.timezone import now
from .models import Booking, Car, User
from .forms import BookingForm, CarForm, UserForm
from datetime import date
from .utils import calculate_total_price, get_greeting

class CarView(View):
    @method_decorator(login_required)
    def get(self, request):
        cars = Car.objects.order_by('name').all()
        return render(request, 'admin/car_list.html', {'cars': cars})
    
    @method_decorator(login_required)
    def post(self, request):
        form = CarForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Car entry created successfully.')
            return redirect('car:index')
        else:
            messages.error(request, 'Invalid or missing data.')
            return render(request, 'admin/car_create.html', {'form': form})

    @method_decorator(login_required)
    def update(self, request, id):
        car = get_object_or_404(Car, id=id)

        if request.method == 'POST':
            form = CarForm(request.POST, request.FILES, instance=car)
            if form.is_valid():
                form.save()
                messages.success(request, 'Car entry updated successfully.')
                return redirect('car:index')
            else:
                messages.error(request, 'Invalid or missing data.')
        else:
            form = CarForm(instance=car)

        return render(request, 'admin/car_update.html', {'form': form, 'car': car})

    @method_decorator(login_required)
    def delete(self, request, id):
        car = get_object_or_404(Car, id=id)
        car.delete()
        messages.success(request, 'Car entry deleted successfully.')
        return redirect('car:index')
    

class UserView(View):
    @method_decorator(login_required)
    def get(self, request):
        users = User.objects.filter(role=0).order_by('name')
        return render(request, 'admin/user_list.html', {'users': users})
    
    @method_decorator(login_required)
    def create(self, request):
        if request.method == 'POST':
            form = UserForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'User created successfully.')
                return redirect('user:index')
            else:
                messages.error(request, 'Invalid or missing data.')
        else:
            form = UserForm()

        template = 'admin/create_user.html'  # Replace with the actual template name
        return render(request, template, {'form': form})

    @method_decorator(login_required)
    def update(self, request, id):
        user = get_object_or_404(User, id=id)

        if request.method == 'POST':
            form = UserForm(request.POST, instance=user)
            new_password = request.POST.get('password')
            confirm_new_password = request.POST.get('confirm_password')

            if form.is_valid():
                if not form.cleaned_data['name'] or not form.cleaned_data['last_name'] or not form.cleaned_data['phone_number'] or not form.cleaned_data['email']:
                    messages.error(request, 'All fields are required.')
                elif new_password and new_password != confirm_new_password:
                    messages.error(request, 'Passwords do not match.')
                else:
                    if new_password:
                        form.instance.password = make_password(new_password)
                    form.save()
                    messages.success(request, 'Profile updated successfully.')

                    if user.role == 0:
                        return redirect('car:available')
                    elif user.role == 1:
                        return redirect('user:admin_dashboard')

                    return redirect('user:index')
            else:
                messages.error(request, 'Invalid or missing data.')
        else:
            form = UserForm(instance=user)

        template = 'admin/update.html' if user.role == 1 else 'user/update.html'

        return render(request, template, {'form': form})

    @method_decorator(login_required)
    def delete(self, request, id):
        user = get_object_or_404(User, id=id)

        if user:
            try:
                user.delete()
                messages.success(request, 'User deleted successfully.')
            except Exception:
                messages.error(request, 'You cannot delete this user, as it has a booking tied to it!')
        else:
            messages.error(request, 'User not found.')

        return redirect('user:index')


class BookingView(View):
    @method_decorator(login_required)
    def create(self, request, car_id):
        today_date = date.today()
        car = get_object_or_404(Car, id=car_id)

        if request.method == 'POST':
            form = BookingForm(request.POST)
            start_date = request.POST.get('start_date')
            end_date = request.POST.get('end_date')

            if form.is_valid():
                user_id = request.user.id

                new_booking = Booking(
                    car_id=car_id,
                    user_id=user_id,
                    start_date=start_date,
                    end_date=end_date
                )
                new_booking.save()

                car.status = 0
                car.save()

                receipt_data = {
                    'customer_name': request.user.name,
                    'customer_last': request.user.last_name,
                    'car_name': car.name,
                    'start_date': start_date,
                    'end_date': end_date,
                    'total_price': calculate_total_price(car.price, start_date, end_date)
                }
                return render(request, 'booking/receipt_modal.html', {'receipt_data': receipt_data})
            else:
                messages.error(request, 'Invalid or missing data.')
        else:
            form = BookingForm()

        return render(request, 'booking/create.html', {'today_date': today_date, 'car': car, 'form': form})

    @method_decorator(login_required)
    def my_bookings(self, request):
        greeting = get_greeting()
        user_id = request.user.id

        bookings = Booking.objects.filter(user_id=user_id).select_related('car').select_related('user').order_by('start_date')

        return render(request, 'booking/index.html', {'greeting': greeting, 'bookings': bookings})

    @method_decorator(login_required)
    def update(self, request, id):
        booking = get_object_or_404(Booking, id=id)
        cars = Car.objects.order_by('name')

        if request.method == 'POST':
            if 'update' in request.POST:
                new_car_id = request.POST.get('car_id')
                start_date = request.POST.get('start_date')
                end_date = request.POST.get('end_date')
            elif 'cancel' in request.POST:
                return redirect('booking:my_bookings')
            error = None

            if not start_date:
                error = 'Start date is required.'
            if not end_date:
                error = 'End date is required.'

            if error is not None:
                messages.error(request, error)
            else:
                old_car_id = booking.car_id
                
                booking.car_id = new_car_id
                booking.start_date = start_date
                booking.end_date = end_date
                booking.save()

                if old_car_id != new_car_id:
                    Car.objects.filter(id=old_car_id).update(status=1)
                    Car.objects.filter(id=new_car_id).update(status=0)

                return redirect('booking:my_bookings')

        return render(request, 'booking/update.html', {'booking': booking, 'cars': cars})

    @method_decorator(login_required)
    def delete(self, request, id):
        booking = get_object_or_404(Booking, id=id)
        car_id = booking.car_id
        booking.delete()

        Car.objects.filter(id=car_id).update(status=1)

        if request.user.role == 1:
            return redirect('booking:index')

        return redirect('booking:my_bookings')
