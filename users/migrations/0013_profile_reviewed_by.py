# Generated by Django 3.1 on 2020-09-03 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_auto_20200831_2050'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='reviewed_by',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
