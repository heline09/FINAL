# Generated by Django 5.0.1 on 2024-03-24 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0018_alter_recruiterprofile_subscription_plan'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recruiterprofile',
            name='subscription_plan',
            field=models.CharField(max_length=100, null=True),
        ),
    ]