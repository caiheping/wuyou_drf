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
from wuyou_drf.settings import MEDIA_ROOT
from django.views.static import serve

# jwt内部实现的登陆视图
from rest_framework_jwt.views import obtain_jwt_token

from base.views import AreasView, BannersView, TestView
from companys.views import CompanyView, JobView, WelfareView
from users.views import UsersView
from resumes.views import ResumeView, ResumeWorkingView, ResumeEducationView, ResumeJobView, ResumeProjectExperienceView


router = DefaultRouter(trailing_slash=False)

# 基础
router.register(r'areas', AreasView)    # 区域
router.register(r'banners', BannersView)    # 轮播图url

# 公司
router.register(r'company', CompanyView)    # 公司
router.register(r'job', JobView)    # 职位
router.register(r'welfare', WelfareView)    # 福利

# 用户
router.register(r'users', UsersView)

# 简历
router.register(r'resume', ResumeView)
router.register(r'resume_projectExperience', ResumeProjectExperienceView)
router.register(r'resume_working', ResumeWorkingView)
router.register(r'resume_education', ResumeEducationView)
router.register(r'resume_job', ResumeJobView)

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^docs/', include_docs_urls(title='无忧API')),
    url(r'^api/(?P<version>\w+)/', include(router.urls)),    # http://127.0.0.1:8080/api/v1
    url(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),  # 用于提供访问media资源
    url('^ueditor/', include('DjangoUeditor.urls')),  # 富文本编辑器
    path(r'login', obtain_jwt_token),
    path(r'test', TestView.as_view()),
]
