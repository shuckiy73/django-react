from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class CustomUser(AbstractUser):
    # Ваши дополнительные поля

    groups = models.ManyToManyField(
        Group,
        verbose_name='Группы',  # Русскоязычное название
        blank=True,
        help_text='Группы, к которым принадлежит пользователь. Пользователь получает все права, предоставленные каждой из его групп.',
        related_name='customuser_groups',
        related_query_name='customuser',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name='Права пользователя',  # Русскоязычное название
        blank=True,
        help_text='Конкретные права для этого пользователя.',
        related_name='customuser_permissions',
        related_query_name='customuser',
    )

    class Meta:
        verbose_name = 'Пользователь'  # Русскоязычное название модели
        verbose_name_plural = 'Пользователи'  # Русскоязычное название модели во множественном числе