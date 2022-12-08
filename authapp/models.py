from django.db import models
from django.contrib.auth.models import AbstractUser
from mainapp.models import NULLABLE


class User(AbstractUser):
    email = models.EmailField(blank=True, verbose_name='Email', unique=True)
    age = models.PositiveIntegerField(verbose_name='Возраст', **NULLABLE)
    avatar = models.ImageField(upload_to='users', **NULLABLE)

    class Meta:
        verbose_name = "пользовтель"
        verbose_name_plural = 'пользователи'
