from django.contrib.auth.models import BaseUserManager

from rest_framework.authtoken.models import Token



class UserManager(BaseUserManager):
    
    def create_user(self, email, password=None, **extra_fields):
        
        if not email:
            raise ValueError('Users must have an email address //')
        
        user = self.model(
            email=self.normalize_email(email),
            **extra_fields
        )

        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_superuser(self, email, password=None, **extra_fields):
        
        user = self.create_user(
            email,
            password=password,
            **extra_fields
        )
        
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        Token.objects.get_or_create(user=user)

        return user