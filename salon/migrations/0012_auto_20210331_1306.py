# Generated by Django 3.1.7 on 2021-03-31 04:06

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('salon', '0011_auto_20210330_1935'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='booking',
            options={'ordering': ['menu']},
        ),
        migrations.RemoveField(
            model_name='booking',
            name='hairMenu',
        ),
        migrations.AddField(
            model_name='booking',
            name='booking_date',
            field=models.DateTimeField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='booking',
            name='menu',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='salon.menu'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='username',
            field=models.TextField(max_length=100),
        ),
    ]
