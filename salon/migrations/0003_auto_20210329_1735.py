# Generated by Django 3.1.7 on 2021-03-29 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salon', '0002_menu_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='photo',
            field=models.ImageField(default='defo', upload_to=None),
        ),
    ]
