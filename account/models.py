from django.db import models
from django.db.models.fields import proxy
from django.urls import reverse
from django.contrib.auth.models import AbstractUser, AbstractBaseUser, BaseUserManager
from django.utils.translation import gettext_lazy
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator
from django.utils import timezone
import uuid

ADMIN = 0
READER = 1
WRITER = 2

class BaseModel(models.Model):
    """BaseModel for every children models"""

    uuid = models.UUIDField(default=uuid.uuid4, editable=False, db_index=True, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class AccountManager(BaseUserManager):
    def create_user(self, email, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser, BaseModel):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    username = models.CharField(unique=True,max_length=64, null = True, blank=True)
    name = models.CharField(max_length=64, null = True, blank=True)
    
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    mobile_number = models.CharField(validators=[phone_regex], max_length=17, blank=True,null = True) 

    user_registered_on = models.DateTimeField(default=timezone.now, blank=True)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = AccountManager()

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email
    
    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

class AdminSecret(BaseModel):
    """Model to store encrypted API key secret for admin user"""
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    # secret = models.BinaryField(max_length=10000)
    api_key = models.CharField(max_length=1000)