# Generated by Django 2.2 on 2020-05-24 08:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('real_name', models.CharField(max_length=20, verbose_name='姓名')),
                ('contact', models.CharField(max_length=18, verbose_name='联系方式')),
                ('email', models.CharField(max_length=20, verbose_name='邮箱地址')),
                ('permissionType', models.CharField(choices=[(0, '管理员'), (1, '开发人员'), (2, '测试人员')], max_length=50, verbose_name='角色')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
            options={
                'verbose_name': '成员信息',
                'verbose_name_plural': '成员信息',
                'db_table': 'ts_profile',
            },
        ),
    ]
