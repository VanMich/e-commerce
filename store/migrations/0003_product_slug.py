# Generated by Django 4.1.5 on 2023-01-28 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(default='', max_length=150),
            preserve_default=False,
        ),
    ]
