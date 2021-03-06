from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser , PermissionsMixin ,BaseUserManager

# Create your models here.


class CustomUserManager(BaseUserManager):

    def create_superuser(self , email , username , first_name, password , **other_fields):

        other_fields.setdefault('is_staff',True)
        other_fields.setdefault('is_active',True)
        other_fields.setdefault('is_superuser',True)

        if other_fields.get('is_staff') is not True:
            return ValueError('superuser must be assigned to is_staff=True')

        if other_fields.get('is_superuser') is not True:
            return ValueError('superuser must be assigned to is_superuser=True')

        return self.create_user(email , username , first_name , password , **other_fields)

    def create_user(self,email,username,first_name,password,**other_fields):

        if not email:
            raise ValueError(_("You must provide email"))

        email = self.normalize_email(email)
        user = self.model(email=email,username=username,first_name=first_name,**other_fields)

        user.set_password(password)
        user.save()
        return user

class NewUser(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(_('email_address'),unique=True)
    username = models.CharField(max_length=150,unique=True)
    first_name = models.CharField(max_length=150,blank=True)
    start_date = models.DateTimeField(default=timezone.now)
    about = models.TextField(_('about'),max_length=400,blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','first_name']

    def __str__(self):
        return self.username
