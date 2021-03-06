# Generated by Django 2.2 on 2020-05-24 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_auto_20200524_1646'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='code',
            field=models.CharField(db_index=True, default='216ace580ffa071f6a22', max_length=50, verbose_name='项目code'),
        ),
        migrations.AlterField(
            model_name='projectmembers',
            name='permissionType',
            field=models.IntegerField(choices=[(0, '管理员'), (1, '开发人员'), (2, '测试人员')], max_length=50, verbose_name='权限角色'),
        ),
    ]
