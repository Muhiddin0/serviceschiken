# Generated by Django 4.2.4 on 2023-11-13 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Delivered',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('phone', models.CharField(max_length=250)),
                ('location', models.CharField(max_length=250)),
                ('price', models.CharField(max_length=250)),
                ('img', models.ImageField(null=True, upload_to='broiler_uploaded')),
                ('comment', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='DeliverUsers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.PositiveIntegerField()),
                ('name', models.CharField(max_length=250)),
                ('phone', models.CharField(max_length=250)),
            ],
        ),
    ]