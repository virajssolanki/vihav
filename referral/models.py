from django.db import models
from django.db import models
from django.utils import timezone
from users.models import User
from django.urls import reverse

STATUS_CHOICES = (
    ('success','success'),
    ('pending', 'pending'),
    ('fail','fail'),
)

ALERT_CHOICES = (
    ('success','green (approved)'),
    ('warning', 'yellow (pending)'),
    ('danger','red (canceled)'),
)

class Referrals(models.Model):
	name = models.CharField(max_length=50)
	number = models.CharField(max_length=10, blank=True)
	date_posted = models.DateTimeField(default=timezone.now)
	amount = models.FloatField(blank=True)
	status = models.CharField(max_length=30, choices=STATUS_CHOICES, blank=True)
	alert = models.CharField(max_length=30, choices=ALERT_CHOICES, blank=True)
	reference = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.name