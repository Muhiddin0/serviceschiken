# Generated by Django 4.2.4 on 2023-11-14 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivered', '0002_alter_delivered_comment_alter_delivered_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='delivered',
            name='comment_img',
            field=models.ImageField(default=1, upload_to='chicken_home'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='delivered',
            name='comment',
            field=models.CharField(max_length=400),
        ),
    ]
