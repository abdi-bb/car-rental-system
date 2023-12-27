# urls.py
from django.urls import include, path
from rest_framework.routers import SimpleRouter
from rest_framework_nested import routers
from . import views


router = routers.DefaultRouter()
router.register('cars', views.CarViewSet)
router.register('customers', views.CustomerViewSet)
router.register('bookings', views.BookingViewSet, basename='bookings')


cars_router = routers.NestedDefaultRouter(router, 'cars', lookup='car')

cars_router.register('reviews', views.ReviewViewSet, basename='car-reviews')
cars_router.register('images', views.CarImageViewSet, basename='car-images')

# urlpatterns = router.urls + cars_router.urls
urlpatterns = [
    path('', include(router.urls)),
    path('', include(cars_router.urls))
    # path('cars/', views.CarList.as_view()),
    # path('cars/<int:pk>/', views.CarDetail.as_view(), name='car-detail'),
    # path('customers/', views.UserList.as_view()),
    # path('customers/<int:pk>/', views.UserDetail.as_view(), name='user-detail'),
    # path('bookings/', views.BookingList.as_view()),
    # path('bookings/<int:pk>/', views.BookingDetail.as_view(), name='booking-detail')
]
