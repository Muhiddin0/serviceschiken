# Generated by Django 4.2.4 on 2023-11-15 13:30

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VetUsers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.PositiveIntegerField()),
                ('name', models.CharField(max_length=250)),
                ('phone', models.CharField(max_length=250)),
                ('status', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='VetClient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('phone', models.CharField(max_length=250)),
                ('location', models.CharField(max_length=250)),
                ('day', models.CharField(max_length=250)),
                ('humidity', models.CharField(max_length=250)),
                ('temperature', models.CharField(max_length=250)),
                ('sickness', models.CharField(max_length=250)),
                ('diagnose', models.CharField(max_length=250)),
                ('img', models.ImageField(null=True, upload_to='images_uploaded')),
                ('create_at', models.DateField(default=datetime.date(2021, 12, 18))),
                ('vet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vet.vetusers')),
            ],
        ),
    ]
