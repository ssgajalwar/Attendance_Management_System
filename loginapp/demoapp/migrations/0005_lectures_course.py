# Generated by Django 5.0.1 on 2024-03-23 17:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demoapp', '0004_recordattendance_latitude_recordattendance_longitude'),
    ]

    operations = [
        migrations.AddField(
            model_name='lectures',
            name='course',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='demoapp.course'),
            preserve_default=False,
        ),
    ]
