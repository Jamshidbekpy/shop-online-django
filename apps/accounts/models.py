from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .manager import CustomUserManager

# Create your models here.
class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    phone = models.CharField(max_length=20, blank=True, null=True)

    objects = CustomUserManager()  # Custom manager

    USERNAME_FIELD = 'email'  # Login qilish uchun email ishlatiladi
    REQUIRED_FIELDS = []  # Superuser yaratishda qo'shimcha maydonlar

    def __str__(self):
        return self.email