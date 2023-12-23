# forms.py
from django import forms
from .models import Booking, Car, User

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
        

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['start_date', 'end_date']

