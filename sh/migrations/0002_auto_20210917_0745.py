# Generated by Django 3.2.7 on 2021-09-17 07:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sh', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shortner',
            name='createdDate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 9, 17, 7, 45, 30, 367619)),
        ),
        migrations.AlterField(
            model_name='shortner',
            name='expirationDate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 9, 17, 8, 45, 30, 367677)),
        ),
        migrations.AlterField(
            model_name='shortner',
            name='urlOriginal',
            field=models.URLField(max_length=512),
        ),
    ]