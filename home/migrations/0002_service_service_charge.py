# Generated by Django 5.0 on 2024-01-16 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='service_charge',
            field=models.PositiveIntegerField(default=2),
            preserve_default=False,
        ),
    ]
