# Generated by Django 2.2.8 on 2020-09-04 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=7),
        ),
    ]
