# Generated by Django 5.0.1 on 2024-02-18 12:05

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('internconnect', '0005_notification_internship_recipient'),
    ]

    operations = [
        migrations.AddField(
            model_name='internship',
            name='expiry_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='internship',
            name='post_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]