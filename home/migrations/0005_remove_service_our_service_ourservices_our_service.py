# Generated by Django 5.0 on 2024-01-18 07:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_remove_service_service_charge_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='our_service',
        ),
        migrations.AddField(
            model_name='ourservices',
            name='our_service',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, related_name='services', to='home.service'),
            preserve_default=False,
        ),
    ]
