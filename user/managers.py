from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext as _

class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where username is the unique identifier
    for authentication instead of usernames.
    """

    def create_user(self, phone_number, username, password, **extra_fields):
        if not username:
            raise ValueError(_('Users must have an username address'))
        username = self.normalize_email(username)
        user = self.model(phone_number=phone_number,
                          username=username,
                          **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, phone_number, username, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(phone_number, username, password, **extra_fields)