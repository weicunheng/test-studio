# Generated by Django 2.2 on 2020-05-24 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='permissionType',
            field=models.IntegerField(choices=[(0, '管理员'), (1, '开发人员'), (2, '测试人员')], verbose_name='角色'),
        ),
    ]
