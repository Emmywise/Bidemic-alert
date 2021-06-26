# Generated by Django 3.2.4 on 2021-06-25 12:11

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('alert', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='merchant',
            name='date_created',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='product',
            name='date_created',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]