# Generated by Django 4.0.6 on 2022-08-01 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_pet_image_alter_pet_purchased_price_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='purchased_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
