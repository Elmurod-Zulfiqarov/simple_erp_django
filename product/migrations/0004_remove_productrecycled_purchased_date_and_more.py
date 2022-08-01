# Generated by Django 4.0.6 on 2022-08-01 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_alter_product_published_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productrecycled',
            name='purchased_date',
        ),
        migrations.AddField(
            model_name='productrecycled',
            name='purchased_price',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
    ]