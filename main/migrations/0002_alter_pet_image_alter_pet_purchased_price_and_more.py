# Generated by Django 4.0.6 on 2022-08-01 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/pet'),
        ),
        migrations.AlterField(
            model_name='pet',
            name='purchased_price',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='pet',
            name='sale_price',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='pet',
            name='sold_out_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
