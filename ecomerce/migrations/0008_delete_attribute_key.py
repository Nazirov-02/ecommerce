# Generated by Django 5.1.5 on 2025-02-04 15:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecomerce', '0007_product_attribute_attribute_value_attribute_key'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Attribute_key',
        ),
    ]
