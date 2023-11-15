
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivered', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='delivered',
            name='comment',
            field=models.ImageField(upload_to='chicken_home'),
        ),
        migrations.AlterField(
            model_name='delivered',
            name='img',
            field=models.ImageField(null=True, upload_to='chicken_uploaded'),
        ),
    ]
