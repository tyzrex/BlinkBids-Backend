# Generated by Django 5.0.2 on 2024-07-07 14:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0007_remove_cart_total_price_alter_cartitems_cart'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitems',
            name='price',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='price',
        ),
    ]
