from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from .managers import UserManager



class User(AbstractBaseUser, PermissionsMixin):
    
    GENDER_CHOICES = [
        ('hombre', 'Hombre'),
        ('mujer', 'Mujer'),
        ('otro', 'Otro')
    ]

    # id
    email =     models.EmailField(unique=True, max_length=255, verbose_name='Correo electronico')
    name =      models.CharField(max_length=255, verbose_name='Nombre')
    last_name = models.CharField(max_length=255, verbose_name='Apellido', blank=True, null=True)
    gender =    models.CharField(max_length=10, choices=GENDER_CHOICES, null=True, blank=True)
    twitter =   models.CharField(max_length=255, blank=True, null=True)
    avatar =    models.ImageField(default='default_avatar/default_avatar_profile.jpg', upload_to='media')
    is_active = models.BooleanField(default=True)
    is_staff =  models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'

    def __str__(self):
        return str(self.id) + ' - ' + self.name + ' - ' + self.email
    
    class Meta:
        db_table = 'Users'
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'