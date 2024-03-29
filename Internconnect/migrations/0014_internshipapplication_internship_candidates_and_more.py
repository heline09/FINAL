# Generated by Django 5.0.1 on 2024-03-07 11:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0014_recruiterprofile_studentprofile_delete_userprofile'),
        ('internconnect', '0013_alter_internship_recruiter'),
    ]

    operations = [
        migrations.CreateModel(
            name='InternshipApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('internship', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='internconnect.internship')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.student')),
            ],
            options={
                'unique_together': {('internship', 'student')},
            },
        ),
        migrations.AddField(
            model_name='internship',
            name='candidates',
            field=models.ManyToManyField(related_name='applied_internships', through='internconnect.InternshipApplication', to='accounts.student'),
        ),
        migrations.DeleteModel(
            name='SelectedSkill',
        ),
    ]
