from django.db import models
from db.base_model import BaseModel

# Create your models here.


class Areas(models.Model):
    aTitle = models.CharField(max_length=20, verbose_name='区域名称')
    is_hot = models.BooleanField(default=False, verbose_name='是否热门')
    parent = models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.aTitle

    class Meta:
        verbose_name = '区域'
        verbose_name_plural = verbose_name


class Banners(BaseModel):
    index = models.IntegerField(default=1, verbose_name='索引')
    image = models.ImageField(upload_to='banner/', verbose_name='图片')
    url = models.CharField(max_length=100, blank=True, null=True, verbose_name='链接地址')

    def __str__(self):
        return self.index

    class Meta:
        verbose_name = '轮播图'
        verbose_name_plural = verbose_name
