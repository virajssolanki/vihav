# Generated by Django 3.1 on 2020-08-20 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('referral', '0008_withdraw'),
    ]

    operations = [
        migrations.AddField(
            model_name='withdraw',
            name='note',
            field=models.TextField(blank=True, max_length=350),
        ),
        migrations.AlterField(
            model_name='withdraw',
            name='alert',
            field=models.CharField(blank=True, choices=[('table-success', 'green (approved)'), ('table-warning', 'yellow (pending)'), ('table-danger', 'red (canceled)')], default='warning', max_length=30),
        ),
    ]
