# Generated by Django 4.1.6 on 2023-02-23 20:59

from django.db import migrations, models
import store.models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_alter_product_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='photo',
            field=models.ImageField(upload_to=store.models.photo_directory_and_name),
        ),
    ]
