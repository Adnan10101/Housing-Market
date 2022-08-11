from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone
# Create your models here.

class UserManager(BaseUserManager):

  def _create_user(self, email,username,is_staff, is_superuser, password, **extra_fields):
    if not email:
        raise ValueError('Users must have an email address')
    now = timezone.now()
    email = self.normalize_email(email)
    user = self.model(
        username = username,
        email=email,
        last_login=now,
        is_staff=is_staff, 
        is_active=True,
        is_superuser=is_superuser, 
        
         
        **extra_fields
    )
    user.set_password(password)
    user.save(using=self._db)
    return user

  def create_user(self, email,username, password, **extra_fields):
    return self._create_user(email, username, False, False,password, **extra_fields)

  def create_superuser(self, email,username, password, **extra_fields):
    user=self._create_user(email, username, True, True,password, **extra_fields)
    return user


class UserModel(AbstractBaseUser,PermissionsMixin):
    
    username = models.CharField(max_length = 30)
    password = models.CharField(max_length = 30)
    email = models.EmailField(unique = True,primary_key=True)
    phone_no = models.CharField(max_length=9)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    last_login = models.DateTimeField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add = True)

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def get_absolute_url(self):
        return "/users/%i/" % (self.pk)

    def __str__(self):
        return self.email