# Generated by Django 5.0.2 on 2024-07-07 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0008_remove_cartitems_price_remove_orderitem_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='is_paid',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='order',
            name='payment_method',
            field=models.CharField(default='a', max_length=50),
            preserve_default=False,
        ),
    ]