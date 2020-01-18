"""wuyou_drf URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url

from rest_framework.routers import DefaultRouter
from rest_framework.documentation import include_docs_urls

# jwt内部实现的登陆视图
from rest_framework_jwt.views import obtain_jwt_token

from base.views import AreasView, BannersView, TestView

router = DefaultRouter(trailing_slash=False)

# 基础
router.register(r'areas', AreasView, base_name="areas")    # 区域
router.register(r'banners', BannersView, base_name="banners")    # 轮播图url

urlpatterns = [
    path('admin', admin.site.urls),
    url(r'^docs/', include_docs_urls(title='无忧API')),
    url(r'^api/(?P<version>\w+)/', include(router.urls)),    # http://127.0.0.1:8080/api/v1
    path(r'login', obtain_jwt_token),
    path(r'test', TestView.as_view()),
]
