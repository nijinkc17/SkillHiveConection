# Generated by Django 5.0 on 2024-01-31 06:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_remove_booking_service_remove_booking_user_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='booking',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='home.bookingpage'),
        ),
    ]
