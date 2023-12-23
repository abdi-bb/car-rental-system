# urls.py
from django.urls import path
from .views import BookingView, CarView, UserView

app_name = 'rental'

urlpatterns = [
    # Car URLs
    path('car_create/', CarView.as_view(), name='car_create'),
    path('car_index/', CarView.as_view(), name='car_index'),
    path('car_update/<int:id>/', CarView.as_view(), name='car_update'),
    path('car_delete/<int:id>/', CarView.as_view(), name='car_delete'),
    
    # User URLs
    path('user_index/', UserView.as_view(), name='user_index'),
    path('user_create/', UserView.as_view(), name='user_create'),  # New URL for user_create
    path('user_update/<int:id>/', UserView.as_view(), name='user_update'),
    path('user_delete/<int:id>/', UserView.as_view(), name='user_delete'),
    
    # Booking URLs
    path('booking_create/<int:car_id>/', BookingView.as_view(), name='booking_create'),
    path('booking_my_bookings/', BookingView.as_view(), name='booking_my_bookings'),
    path('booking_update/<int:id>/', BookingView.as_view(), name='booking_update'),
    path('booking_delete/<int:id>/', BookingView.as_view(), name='booking_delete'),
]
