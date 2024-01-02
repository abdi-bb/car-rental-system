from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext as _

from .managers import CustomUserManager

class User(AbstractUser):
    email = models.EmailField(verbose_name='email', max_length=60, unique=True)
    username = models.CharField(max_length=30, unique=True)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    phone_number = models.CharField(max_length=30)
    

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ('email', 'first_name', 'last_name', 'phone_number')

    objects = CustomUserManager()

    def __str__(self):
        return f'{self.username}, {self.email}'