# Generated by Django 4.0.3 on 2022-03-07 07:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_product_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shippingaddress',
            name='shippingPrice',
        ),
    ]