# Generated by Django 5.1.5 on 2025-02-04 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecomerce', '0009_img_is_main'),
    ]

    operations = [
        migrations.AlterField(
            model_name='img',
            name='image',
            field=models.ImageField(default=1, upload_to='img'),
            preserve_default=False,
        ),
    ]
