"""bbs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from django.views.static import serve
from django.conf import settings
from blog import views
from blog import urls as blog_urls
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^reg/', views.reg),
    #登陆
    url(r'^login/', views.login),
    #注销
    url(r'^logout/', views.logout),
    url(r'^index/', views.index),
    url(r'^pc-geetest/register', views.get_geetest),
    #注册url
    url(r'^reg/', views.register),
    #检测用户名是否已经存在
    url(r'^check_username_exits/', views.check_username_exits),
    #用户上传的文件路由
    url(r'^media/(?P<path>.*)$',serve,{"document_root":settings.MEDIA_ROOT}),
    # 个人博客的处理url
    url(r'^blog/', include(blog_urls)),
    #后台管理

    #添加文章
    url(r'^backend/addarticle/', views.addarticle),
    #图片上传
    url(r'^upload/', views.upload),
    #文章编辑
    url(r'^edit/article/(?P<article_pk>\d+)/', views.edit_article),
    #删除文章
    url(r'^delete/article/(\d*)/',views.delete_article)


]
