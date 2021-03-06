# Generated by Django 3.1 on 2020-08-20 10:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('referral', '0007_auto_20200820_0130'),
    ]

    operations = [
        migrations.CreateModel(
            name='withdraw',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('amount', models.FloatField(blank=True, default=0)),
                ('status', models.CharField(choices=[('success', 'success'), ('pending', 'pending'), ('fail', 'fail')], default='pending', max_length=30)),
                ('alert', models.CharField(blank=True, choices=[('success', 'green (approved)'), ('warning', 'yellow (pending)'), ('danger', 'red (canceled)')], default='warning', max_length=30)),
                ('holder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
