# Generated by Django 2.0.7 on 2018-09-10 02:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productapi', '0003_auto_20180910_0729'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rated',
            name='camera_ratings',
            field=models.DecimalField(decimal_places=2, max_digits=3),
        ),
        migrations.AlterField(
            model_name='rated',
            name='design_ratings',
            field=models.DecimalField(decimal_places=2, max_digits=3),
        ),
        migrations.AlterField(
            model_name='rated',
            name='features_ratings',
            field=models.DecimalField(decimal_places=2, max_digits=3),
        ),
        migrations.AlterField(
            model_name='rated',
            name='performance_ratings',
            field=models.DecimalField(decimal_places=2, max_digits=3),
        ),
        migrations.AlterField(
            model_name='rated',
            name='sound_ratings',
            field=models.DecimalField(decimal_places=2, max_digits=3),
        ),
        migrations.AlterField(
            model_name='smartphone',
            name='camera_ratings',
            field=models.DecimalField(decimal_places=2, max_digits=3),
        ),
        migrations.AlterField(
            model_name='smartphone',
            name='design_ratings',
            field=models.DecimalField(decimal_places=2, max_digits=3),
        ),
        migrations.AlterField(
            model_name='smartphone',
            name='features_ratings',
            field=models.DecimalField(decimal_places=2, max_digits=3),
        ),
        migrations.AlterField(
            model_name='smartphone',
            name='performance_ratings',
            field=models.DecimalField(decimal_places=2, max_digits=3),
        ),
        migrations.AlterField(
            model_name='smartphone',
            name='sound_ratings',
            field=models.DecimalField(decimal_places=2, max_digits=3),
        ),
        migrations.AlterField(
            model_name='smartphone',
            name='total_ratings',
            field=models.DecimalField(decimal_places=2, max_digits=3),
        ),
    ]
