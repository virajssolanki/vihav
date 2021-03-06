# Generated by Django 3.1 on 2020-08-13 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('referral', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='referrals',
            name='alert',
            field=models.CharField(blank=True, choices=[('success', 'success'), ('warning', 'warning'), ('danger', 'danger')], max_length=30),
        ),
        migrations.AlterField(
            model_name='referrals',
            name='name',
            field=models.TextField(max_length=50),
        ),
    ]
