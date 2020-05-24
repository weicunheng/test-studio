# -*- coding: utf-8 -*-
import secrets
from django.contrib.auth.models import User
from django.db import models
from django.db.models.deletion import SET_NULL, CASCADE
from django.utils.translation import ugettext as _

from studioapps.constants.constants import LogoImgSavePathEnum
from studioapps.project import constants, utils
from studioapps.account.models import UserProfile


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
    name = models.CharField(max_length=50, unique=True, help_text="项目名称")
    code = models.CharField(max_length=50, db_index=True, default=utils.gen_project_code(), verbose_name=_("项目code"))
    introduction = models.CharField(max_length=100, verbose_name=_("项目简介"))
    creator = models.ForeignKey(to=User, blank=True, null=True, help_text="创建者", on_delete=models.SET_NULL)
    creator_name = models.CharField(max_length=30, verbose_name=_("创建者姓名"))
    state = models.SmallIntegerField(choices=constants.APP_STATUS_CHOICES, help_text="app的开发状态",
                                     default=constants.AppStatusEnum.LOCAL)
    tags = models.ForeignKey(AppTags, null=True, blank=True, on_delete=SET_NULL, help_text="项目标签")
    language = models.SmallIntegerField(choices=constants.APP_LANGUAGE_CHOICES, default=constants.AppLanguage.PYTHON,
                                        help_text="应用开发语言")
    logo = models.ImageField(blank=True, null=True, upload_to=LogoImgSavePathEnum.API)
    is_delete = models.BooleanField(default=False, verbose_name="是否删除")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name=_("创建时间"))

    def __str__(self):
        return '项目:%s' % self.name

    class Meta:
        db_table = "ts_project"
        verbose_name = "项目信息"
        verbose_name_plural = verbose_name


class ProjectEnvironment(models.Model):
    project = models.ForeignKey(to='project.Project', on_delete=CASCADE, verbose_name=_("所属项目"))
    project_name = models.CharField(max_length=50, verbose_name=_("项目名称"))
    environ = models.IntegerField(default=constants.ProjectEnvironmentEnum.LOCAL,
                                  choices=constants.PROJECT_ENVIRON_CHOICES, verbose_name=_("项目环境"))
    domain = models.URLField(max_length=100, verbose_name=_("域名"))

    def __str__(self):
        return '%s-%s-%s' % (self.project.name, self.environ, self.domain)

    @classmethod
    def create_by_project(cls, project_id, environ, domain):
        try:
            Project.objects.get(pk=project_id)
            ProjectEnvironment(project_id=project_id, environ=environ, domain=domain).save(
                ['project_id', 'environ', 'domain'])
            return True, None
        except Project.DoesNotExist:
            return False, 'ERROR_NOT_EXIST_PROJECT'
        except Exception as e:
            # TODO:
            print("项目环境域名配置异常:{}".format(e))
            return False, 'ERROR_NOT_EXIST_PROJECT'

    class Meta:
        db_table = "ts_project_environ"
        verbose_name = "项目环境域名配置"
        verbose_name_plural = verbose_name


class ProjectMembers(models.Model):
    user = models.ForeignKey(User, related_name='member_user', on_delete=models.CASCADE, verbose_name=_('用户'))
    name = models.CharField(max_length=20, verbose_name=_("人员姓名"))
    profile = models.ForeignKey(to=UserProfile, on_delete=models.CASCADE, verbose_name=_("人员信息"))
    permissionType = models.IntegerField(max_length=50, verbose_name=_('权限角色'), choices=constants.PERMISSION_TYPE_CHOICES)
    project = models.ForeignKey(Project, related_name='member_project', on_delete=models.CASCADE,
                                verbose_name=_('所属项目'))

    class Meta:
        db_table = "ts_project_members"
        verbose_name = "项目成员配置"
        verbose_name_plural = verbose_name
