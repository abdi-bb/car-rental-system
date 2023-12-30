# # urls.py
# from django.urls import include, path
# from rest_framework_nested import routers
# from . import views


# router = routers.DefaultRouter()
# router.register('cars', views.CarViewSet)
# # router.register('customers', views.CustomerViewSet)


# cars_router = routers.NestedDefaultRouter(router, 'cars', lookup='car')

# cars_router.register('reviews', views.ReviewViewSet, basename='car-reviews')
# cars_router.register('images', views.CarImageViewSet, basename='car-images')

# # urlpatterns = router.urls + cars_router.urls
# urlpatterns = [
#     path('', include(router.urls)),
#     path('', include(cars_router.urls))
# ]
