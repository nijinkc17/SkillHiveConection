# Generated by Django 5.0 on 2024-01-31 06:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_remove_booking_professional'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='service',
        ),
    ]
