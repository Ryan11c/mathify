# Generated by Django 5.1.1 on 2024-10-09 01:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0006_alter_post_body'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='title_tag',
        ),
    ]
