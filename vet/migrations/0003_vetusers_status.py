# Generated by Django 4.2.4 on 2023-11-14 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vet', '0002_remove_vetclient_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='vetusers',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]