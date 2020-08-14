# Generated by Django 3.1 on 2020-08-09 18:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Referrals',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=350)),
                ('number', models.CharField(blank=True, max_length=10)),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('amount', models.FloatField(blank=True)),
                ('status', models.CharField(blank=True, choices=[('success', 'success'), ('pending', 'pending'), ('fail', 'fail')], max_length=30)),
                ('reference', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]