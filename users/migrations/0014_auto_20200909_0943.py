# Generated by Django 3.1 on 2020-09-09 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_profile_reviewed_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='credit',
            field=models.FloatField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='profile',
            name='membership',
            field=models.CharField(blank=True, choices=[('Silver', 'Silver'), ('Gold', 'Gold'), ('Platinum', 'Platinum')], max_length=100),
        ),
    ]
