# Generated by Django 2.0.7 on 2019-01-18 09:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_auto_20181223_2104'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userinfo',
            name='country',
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='website',
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='work',
        ),
    ]
