from django.contrib.auth.models import (
     BaseUserManager
)
from django.db import transaction


class UserManager(BaseUserManager):

    def _create_user(self, userName, password, **extra_fields):
        """
        Creates and saves a User with the given email,and password.
        """
        if not userName:
            raise ValueError('The given userName must be set')
        try:
            with transaction.atomic():
                user = self.model(userName=userName, **extra_fields)
                user.set_password(password)
                user.save(using=self._db)
                return user
        except:
            raise

    def create_user(self, userName, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(userName, password, **extra_fields)

    def create_superuser(self, userName, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self._create_user(userName, password=password, **extra_fields)
