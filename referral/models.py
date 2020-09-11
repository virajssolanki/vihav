from django.db import models
from django.db import models
from django.utils import timezone
from users.models import User
from django.urls import reverse

STATUS_CHOICES = (
    ('success','success'),
    ('not reviewed','not reviewed'),
    ('pending', 'pending'),
    ('fail','fail'),
)

ALERT_CHOICES = (
    ('success','green (approved)'),
    ('warning', 'yellow (pending)'),
    ('danger','red (canceled)'),
)

W_ALERT_CHOICES = (
    ('table-success','green (approved)'),
    ('table-warning', 'yellow (pending)'),
    ('table-danger','red (canceled)'),
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
    ('Not Sure ', 'Not Sure'),
)

class Referrals(models.Model):
	name = models.CharField(max_length=50, blank=False, default='')
	last_name = models.CharField(max_length=50, blank=False, default='')
	contact_number = models.CharField(max_length=10, blank=False, default='')
	email = models.EmailField(blank=True)
	city = models.CharField(max_length=100, blank=True)
	date_posted = models.DateTimeField(default=timezone.now)
	amount = models.FloatField(blank=True, default=0)
	status = models.CharField(max_length=30, default='not reviewed', choices=STATUS_CHOICES)
	site = models.CharField(max_length=30, blank=True, choices=SITES)
	alert = models.CharField(max_length=30, default='warning', choices=ALERT_CHOICES, blank=True)
	note = models.TextField(max_length=150, blank=True)
	reference = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.name

class Withdraw(models.Model):
	date_posted = models.DateTimeField(default=timezone.now)
	amount = models.IntegerField(blank=True, default=0)
	note = models.TextField(max_length=150, default='---', blank=True)
	status = models.CharField(max_length=30, default='not reviewed', choices=STATUS_CHOICES)
	alert = models.CharField(max_length=30, default='table-warning', choices=W_ALERT_CHOICES, blank=True)
	holder = models.ForeignKey(User, on_delete=models.CASCADE)