# Generated by Django 4.2.5 on 2024-02-24 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_remove_userprofile_skills'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='skills',
            field=models.ManyToManyField(related_name='user', to='accounts.skill'),
        ),
    ]