# Generated by Django 2.0 on 2018-06-13 10:59

import datetime
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testmanage', '0006_auto_20180613_1058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test_project',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 6, 13, 10, 59, 54, 609220), verbose_name='开始时间'),
        ),
        migrations.AlterField(
            model_name='test_task',
            name='res_person',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL, verbose_name='参与者'),
        ),
        migrations.AlterField(
            model_name='test_version',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 6, 13, 10, 59, 54, 610220), verbose_name='开始时间'),
        ),
    ]
