#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "wls"
# Date: 2019/10/23


from django.conf.urls import url
from blog import views
#blog/xiaohei/archive/2019-08
urlpatterns = [
    url(r'^comment/tree/(\d+)/',views.comment_tree),
    url(r'^comment/(\d+)/',views.comment),

    url(r'^up_down/',views.up_down),
    # url(r'^(\w+)/(category|tag|archive)/(\w+)',views.three_on),
    url(r'^(\w+)/category/(\w+)',views.category_url_handle),
    url(r'^(\w+)/tag/(\w+)',views.tag_url_handle),
    url(r'^(\w+)/archive/(\d{4}-\d{2})',views.archive_url_handle),
    url(r'^(\w+)/article/(\d+)',views.article_detail),
    url(r'^(\w+)',views.home),
    #文章分类处理url  category/NBA

]


