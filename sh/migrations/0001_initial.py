# Generated by Django 3.2.7 on 2021-09-17 07:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shortner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('urlHash', models.CharField(max_length=16, verbose_name='ULR Hash')),
                ('urlOriginal', models.CharField(max_length=512, verbose_name='ULR')),
                ('createdDate', models.DateTimeField(blank=True, default=datetime.datetime(2021, 9, 17, 7, 35, 34, 757315))),
                ('expirationDate', models.DateTimeField(blank=True, default=datetime.datetime(2021, 9, 17, 8, 35, 34, 757366))),
            ],
        ),
    ]
