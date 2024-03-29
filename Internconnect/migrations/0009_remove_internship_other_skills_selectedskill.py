# Generated by Django 4.2.5 on 2024-02-26 13:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0012_alter_customuser_role'),
        ('internconnect', '0008_internship_skills'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='internship',
            name='other_skills',
        ),
        migrations.CreateModel(
            name='SelectedSkill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skills', models.ManyToManyField(to='accounts.skill')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
