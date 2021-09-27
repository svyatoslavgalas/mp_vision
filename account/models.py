from django.contrib.auth.models import (
    BaseUserManager,
    AbstractBaseUser,
    PermissionsMixin
)
from django.db import models



class UserManager(BaseUserManager):

    def create_user(
            self, username, password=None, is_staff=False, is_active=True, **extra_fields
    ):
        username = UserManager.normalize_email(username)

        user = self.model(
            username=username, is_active=is_active, is_staff=is_staff, **extra_fields
        )
        if password:
            user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        return self.create_user(
            username, password, is_staff=True, is_superuser=True, **extra_fields
        )


class User(AbstractBaseUser, PermissionsMixin):
    username = models.EmailField('Email', unique=True)
    first_name = models.CharField('Имя', max_length=256, blank=True)
    last_name = models.CharField('Фамилия', max_length=256, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField('Дата регистрации', auto_now_add=True, editable=False)
    wb_token = models.CharField(max_length=256)

    USERNAME_FIELD = "username"

    objects = UserManager()

