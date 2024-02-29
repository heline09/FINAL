# Generated by Django 4.2.5 on 2024-02-29 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_delete_payment'),
        ('internconnect', '0010_remove_internship_recipient_notification_recipient'),
    ]

    operations = [
        migrations.AddField(
            model_name='internship',
            name='fields_of_study',
            field=models.ManyToManyField(related_name='internships', to='accounts.fieldofstudy'),
        ),
    ]
