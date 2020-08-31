from django.db import models
from django.utils import timezone
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _

class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self, email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)

class User(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

IAM_CHOICES = (
    ('Vihav\'s client', 'Vihav\'s client'),
    ('Vihav\'s employee', 'Vihav\'s employee'),
    ('Vendor or Suppliers', 'Vendor or Supplier'),
    ('Channel partner', 'Channel partner'),
    ('Other', 'Other'),
)

SITES = (
    ('KEYSTONE SKYVILLAS', 'KEYSTONE SKYVILLAS'),
    ('WEALTH SQUARE', 'WEALTH SQUARE'),
    ('VIHAV BUSINESS SQUARE', 'VIHAV BUSINESS SQUARE'),
    ('VIHAV SUPREMUS', 'VIHAV SUPREMUS'),
    ('VIHAV SKYONE', 'VIHAV SKYONE'),
    ('VIHAV TRADE CENTRE', 'VIHAV TRADE CENTRE'),
    ('VIHAV KEYSTONE MANSIONS', 'VIHAV KEYSTONE MANSIONS'),
    ('VIHAV KEYSTONE MANSIONS-2', 'VIHAV KEYSTONE MANSIONS-2'),
    ('VIHAV ELITE SQUARE', 'VIHAV ELITE SQUARE'),
    ('VIAHV EXCELUS', 'VIAHV EXCELUS'),
    ('VIHAV ENSIGN', 'VIHAV ENSIGN'),
)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now)
    name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    number = models.CharField(max_length=10, blank=True)
    city = models.CharField(max_length=100, blank=True)
    i_am = models.CharField(max_length=40, blank=True, choices=IAM_CHOICES)
    site = models.CharField(max_length=100, blank=True, choices=SITES)
    verified = models.BooleanField(default=False)
    is_client = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user.profile.name} Profile'


ACC_TYPE_CHOICES = (
    ('current','current'),
    ('saving', 'saving'),
)

class Bank(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now)
    account_holder_name = models.CharField(max_length=100, default="")
    bank_name = models.CharField(max_length=100, default="")
    branch = models.CharField(max_length=100, default="")
    IFSC_code = models.CharField(max_length=10, default="")
    account_number = models.CharField(max_length=40, default="")
    account_type = models.CharField(max_length=100, default="", choices=ACC_TYPE_CHOICES)
 
    def __str__(self):
        return f'{self.user.profile.name} Bank'