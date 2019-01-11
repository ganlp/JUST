# Generated by Django 2.0 on 2018-09-27 18:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testmanage', '0015_auto_20180927_1144'),
        ('casemanage', '0009_auto_20180927_1145'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApiAuto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='自动化版本名称')),
                ('remark', models.TextField(blank=True, max_length=128, verbose_name='备注')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testmanage.test_project', verbose_name='项目名称')),
            ],
            options={
                'verbose_name': '接口自动化',
                'verbose_name_plural': '接口自动化',
            },
        ),
        migrations.AlterModelOptions(
            name='case_catagory',
            options={'verbose_name': '功能菜单', 'verbose_name_plural': '功能菜单'},
        ),
    ]
