# Generated by Django 2.0.7 on 2019-02-10 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productapi', '0017_auto_20190129_1344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='smartphone',
            name='image',
            field=models.ImageField(blank='False', upload_to='media'),
        ),
    ]
