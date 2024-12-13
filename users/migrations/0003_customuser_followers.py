# Generated by Django 5.1.3 on 2024-12-12 17:41

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_customuser_profile_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='followers',
            field=models.ManyToManyField(blank=True, related_name='following', to=settings.AUTH_USER_MODEL),
        ),
    ]
