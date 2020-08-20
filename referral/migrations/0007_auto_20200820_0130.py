# Generated by Django 3.1 on 2020-08-19 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('referral', '0006_auto_20200820_0101'),
    ]

    operations = [
        migrations.AddField(
            model_name='referrals',
            name='note',
            field=models.TextField(blank=True, max_length=350),
        ),
        migrations.AlterField(
            model_name='referrals',
            name='alert',
            field=models.CharField(blank=True, choices=[('success', 'green (approved)'), ('warning', 'yellow (pending)'), ('danger', 'red (canceled)')], default='warning', max_length=30),
        ),
        migrations.AlterField(
            model_name='referrals',
            name='amount',
            field=models.FloatField(blank=True, default=0),
        ),
    ]
