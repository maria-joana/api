from django.contrib.auth.models import AbstractBaseUser
from django.db import models
from .managers import UserManager


class UserModel(AbstractBaseUser):

    username = models.CharField(
        verbose_name='Username',
        max_length=32,
        unique=True
        )
    first_name = models.CharField(
        verbose_name='First Name',
        max_length=32
        )
    last_name = models.CharField(
        verbose_name='Last Name',
        max_length=32)
    email = models.EmailField(
        verbose_name='Email Address',
        max_length=60,
        unique=True)
    date_of_birth = models.DateField(
        verbose_name='Date of Birth',
        null=True,
        blank=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = UserManager()
    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email

    @property
    def is_staff(self):
        return self.is_admin

    class Meta:
        db_table = 'user'
        verbose_name = 'User'
        verbose_name_plural = 'Users'
