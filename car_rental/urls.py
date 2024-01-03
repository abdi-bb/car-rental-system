"""
URL configuration for car_rental project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
import debug_toolbar

schema_view = get_schema_view(
    openapi.Info(
        title="Car Rental System",
        default_version='1.0.0',
        description="API for Car Rental System",
        # terms_of_service="https://www.wheelsonrent.com/terms/",
        # contact=openapi.Contact(email="contact@wheelsonrent.com"),
        # license=openapi.License(name="MIT License"),
    ),
    public=True,
)
    
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('accounts/', include('_auth.urls')),
    path('api/v1/', include('booking.api.v1.urls')),
    path('api/v1/', include('car.api.v1.urls')),
    # path('api/v1/', include('customer.api.v1.urls')),
    # path('api/v1/', include('payment.api.v1.urls')),
    
    path('api/v1/auth/', include('djoser.urls')),
    path('api/v1/auth/', include('djoser.urls.jwt')),
    
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),  # Add this line for ReDoc
    
    path("__debug__/", include(debug_toolbar.urls)),
    
]

from django.conf.urls.static import static
from django.conf import settings

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
