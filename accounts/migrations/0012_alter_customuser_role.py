# Generated by Django 4.2.5 on 2024-02-26 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_alter_customuser_skills'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='role',
            field=models.CharField(choices=[('student', 'Student'), ('recruiter', 'Recruiter')], default='student', max_length=100),
        ),
    ]
