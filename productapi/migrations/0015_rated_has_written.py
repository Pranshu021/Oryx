# Generated by Django 2.0.7 on 2019-01-10 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productapi', '0014_rated_about'),
    ]

    operations = [
        migrations.AddField(
            model_name='rated',
            name='has_written',
            field=models.BooleanField(default=False),
        ),
    ]
