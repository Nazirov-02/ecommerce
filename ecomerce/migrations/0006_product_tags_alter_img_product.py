# Generated by Django 5.1.5 on 2025-02-03 18:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecomerce', '0005_alter_product_discount_alter_product_shipping_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='tags',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='img',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='images', to='ecomerce.product'),
        ),
    ]
