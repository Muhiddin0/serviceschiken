# Generated by Django 4.1.7 on 2023-08-28 23:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0003_remove_user_is_register_remove_user_last_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='referal_money',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
