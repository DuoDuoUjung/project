# Generated by Django 2.2.28 on 2024-11-14 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('friends_app', '0002_user_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='avatars/'),
        ),
    ]
