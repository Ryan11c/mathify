# Generated by Django 5.1.2 on 2024-10-12 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0009_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='images/profile/'),
        ),
    ]