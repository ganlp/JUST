# Generated by Django 2.0 on 2018-06-13 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('casemanage', '0002_auto_20180613_1509'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case',
            name='prepro',
            field=models.TextField(blank=True, max_length=128, verbose_name='前置条件'),
        ),
        migrations.AlterField(
            model_name='case',
            name='remark',
            field=models.TextField(blank=True, max_length=128, verbose_name='备注'),
        ),
    ]
