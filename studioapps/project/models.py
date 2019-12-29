# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models
from django.db.models.deletion import SET_NULL, CASCADE
from django.utils.translation import ugettext as _

from studioapps.constants.constants import LogoImgSavePathEnum
from studioapps.project import constants


class AppTags(models.Model):
    name = models.CharField(max_length=50, unique=True, help_text="分类名称")
    code = models.CharField(max_length=30, unique=True, help_text="代码编号")

    def __unicode__(self):
        return self.__str__()

    def __str__(self):
        return self.name

    class Meta:
        db_table = "ts_apptags"
        verbose_name = "应用分类"
        verbose_name_plural = verbose_name


class Project(models.Model):
    """
    项目的基本信息
    """
    name = models.CharField(max_length=20, unique=True, help_text="项目名称")
    introduction = models.TextField("项目简介")
    creator = models.ForeignKey(to=User, blank=True, null=True, help_text="创建者", on_delete=models.SET_NULL)
    state = models.SmallIntegerField(choices=constants.APP_STATUS_CHOICES, help_text="app的开发状态",
                                     default=constants.AppStatusEnum.LOCAL)
    tags = models.ForeignKey(AppTags, null=True, blank=True, on_delete=SET_NULL, help_text="项目标签")
    language = models.SmallIntegerField(choices=constants.APP_LANGUAGE_CHOICES, default=constants.AppLanguage.PYTHON,
                                        help_text="应用开发语言")
    logo = models.ImageField(blank=True, null=True, upload_to=LogoImgSavePathEnum.API)
    is_delete = models.BooleanField(default=False, verbose_name="是否删除")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name=_("创建时间"))

    class Meta:
        db_table = "ts_project"
        verbose_name = "项目信息"
        verbose_name_plural = verbose_name


class ProjectEnvironment(models.Model):
    project = models.ForeignKey(to='project.Project', on_delete=CASCADE, verbose_name=_("所属项目"))
    environ = models.IntegerField(default=constants.ProjectEnvironmentEnum.LOCAL,
                               choices=constants.PROJECT_ENVIRON_CHOICES, verbose_name=_("项目环境"))
    domain = models.URLField(max_length=100, verbose_name=_("域名"))

    def __str__(self):
        return '%s-%s-%s' % (self.project.name, self.environ, self.domain)

    class Meta:
        db_table = "ts_project_environ"
        verbose_name = "项目环境域名配置"
        verbose_name_plural = verbose_name
