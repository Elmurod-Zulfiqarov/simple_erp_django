# Generated by Django 4.0.6 on 2022-08-01 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_product_quantity_alter_product_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='published_date',
            field=models.DateField(auto_now=True),
        ),
    ]
