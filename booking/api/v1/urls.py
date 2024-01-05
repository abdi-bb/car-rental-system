# urls.py
from django.urls import include, path
from rest_framework_nested import routers
from . import views


router = routers.DefaultRouter()
router.register('bookings', views.BookingViewSet, basename='bookings')

# urlpatterns = router.urls + cars_router.urls
urlpatterns = [
    path('', include(router.urls)),
]