# Generated by Django 5.0.1 on 2024-03-21 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('internconnect', '0021_alter_internship_max_responses'),
    ]

    operations = [
        migrations.AddField(
            model_name='internship',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
