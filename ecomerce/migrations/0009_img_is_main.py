# Generated by Django 5.1.5 on 2025-02-04 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecomerce', '0008_delete_attribute_key'),
    ]

    operations = [
        migrations.AddField(
            model_name='img',
            name='is_main',
            field=models.BooleanField(default=False),
        ),
    ]
