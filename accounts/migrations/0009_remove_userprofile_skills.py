# Generated by Django 4.2.5 on 2024-02-22 19:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_userprofile_skills'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='skills',
        ),
    ]
