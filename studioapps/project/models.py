from django.db import models
from django.db.models.deletion import SET_NULL
from constants.constants import LogoImgSavePathEnum
from studioapps.project.constants import AppStatusEnum, APP_STATUS_CHOICES, AppLanguage, APP_LANGUAGE_CHOICES


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
    creater = models.CharField(max_length=20, help_text="创建者")
    state = models.SmallIntegerField(choices=APP_STATUS_CHOICES, help_text="app的开发状态",
                                     default=AppStatusEnum.LOCAL.value)
    tags = models.ForeignKey(AppTags, null=True, blank=True, on_delete=SET_NULL, help_text="项目分类")
    language = models.SmallIntegerField(choices=APP_LANGUAGE_CHOICES, default=AppLanguage.PYTHON, help_text="应用开发语言")
    logo = models.ImageField(blank=True, null=True, upload_to=LogoImgSavePathEnum.API)

    class Meta:
        db_table = "ts_project"
        verbose_name = "项目信息"
        verbose_name_plural = verbose_name
