# Generated by Django 3.2.16 on 2022-12-16 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopCrud', '0004_remove_product_specs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.CharField(default='', max_length=1000),
        ),
    ]
