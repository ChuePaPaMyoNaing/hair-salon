# Generated by Django 3.1.7 on 2021-03-29 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salon', '0003_auto_20210329_1735'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='photo',
            field=models.ImageField(upload_to=None),
        ),
    ]
