from django.db import models
from db.base_model import BaseModel
# Create your models here.


class Company(BaseModel):
    """公司"""
    Company_Type = (
        (1, "国企"),
        (2, "外企"),
        (3, "民营"),
    )
    name = models.CharField(max_length=30, verbose_name='公司名')
    type = models.IntegerField(choices=Company_Type, verbose_name="公司类型", help_text="公司类型")
    addr = models.CharField(max_length=100, verbose_name='公司详细地址')
    area = models.CharField(max_length=100, verbose_name='所属区域')
    introduce = models.TextField(blank=True, null=True, verbose_name='介绍')
    personnel = models.IntegerField(default=1, verbose_name='人员')
    company_start_time = models.DateField(null=True, blank=True, verbose_name="成立时间")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '公司'
        verbose_name_plural = verbose_name


class Job(BaseModel):
    """发布职位"""
    Education_Type = (
        (1, "不限"),
        (2, "大专"),
        (3, "本科"),
        (4, "硕士"),
    )
    job = models.CharField(max_length=20, verbose_name='职业')
    company = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name='公司', related_name='company')
    min_salary = models.IntegerField(verbose_name='最小薪水')
    max_salary = models.IntegerField(verbose_name='最大薪水')
    describe = models.TextField(verbose_name='描述')
    working_min_years = models.IntegerField(null=True, blank=True, verbose_name='最小工龄')
    working_max_years = models.IntegerField(null=True, blank=True, verbose_name='最大工龄')
    education = models.IntegerField(choices=Education_Type, verbose_name='学历')
    recruitment = models.IntegerField(default=1, verbose_name='招聘人数')
    city = models.CharField(max_length=20, verbose_name='发布城市')

    class Meta:
        verbose_name = '职位'
        verbose_name_plural = verbose_name


class Welfare(BaseModel):
    """公司福利"""
    name = models.CharField(max_length=20, verbose_name='名称')
    company = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name='公司')

    class Meta:
        verbose_name = '福利'
        verbose_name_plural = verbose_name
