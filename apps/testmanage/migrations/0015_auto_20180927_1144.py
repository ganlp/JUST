# Generated by Django 2.0 on 2018-09-27 11:44

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('testmanage', '0014_auto_20180720_1559'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test_project',
            name='start_time',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='开始时间'),
        ),
        migrations.AlterField(
            model_name='test_version',
            name='start_time',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='开始时间'),
        ),
    ]
