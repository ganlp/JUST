# Generated by Django 2.0 on 2018-09-27 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('casemanage', '0007_auto_20180720_1559'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='case_catagory',
            options={'verbose_name': '功能菜单', 'verbose_name_plural': '功能菜单'},
        ),
        migrations.AlterField(
            model_name='case_catagory',
            name='upper_case',
            field=models.IntegerField(blank=True, null=True, verbose_name='上级分类ID'),
        ),
    ]
