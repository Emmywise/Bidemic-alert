# Generated by Django 3.2.4 on 2021-06-25 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alert', '0006_alter_product_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_alert',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]