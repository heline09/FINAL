# Generated by Django 5.0.1 on 2024-03-14 15:46

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0007_rename_cover_letter_application_application_message_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='apply_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]