# Generated by Django 3.1.7 on 2021-03-30 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salon', '0007_auto_20210330_1738'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='photo1',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
