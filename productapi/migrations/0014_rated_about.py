# Generated by Django 2.0.7 on 2019-01-07 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productapi', '0013_auto_20180913_0137'),
    ]

    operations = [
        migrations.AddField(
            model_name='rated',
            name='about',
            field=models.TextField(blank=True, max_length=500),
        ),
    ]
