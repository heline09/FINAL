# Generated by Django 5.0.1 on 2024-03-24 19:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0019_alter_recruiterprofile_subscription_plan'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recruiterprofile',
            name='subscription_plan',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.subscriptionplan'),
        ),
    ]
