# Generated by Django 4.0.6 on 2022-08-01 06:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated at')),
                ('full_name', models.CharField(max_length=256)),
                ('definition', models.TextField(blank=True, max_length=4096, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='account/stuff')),
                ('specialty', models.CharField(max_length=256)),
                ('salary', models.CharField(blank=True, max_length=255, null=True)),
                ('gender', models.CharField(choices=[('female', 'female'), ('male', 'male')], max_length=8)),
                ('passport', models.FileField(blank=True, null=True, upload_to='')),
                ('phone', models.CharField(blank=True, max_length=32, null=True)),
                ('phone_farm', models.CharField(blank=True, max_length=32, null=True)),
                ('telegram', models.CharField(blank=True, max_length=128, null=True)),
                ('created_by', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_createdby', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_modifiedby', to=settings.AUTH_USER_MODEL)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='staff', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
