#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "wls"
# Date: 2019/10/23

from django import template
from blog import models
from django.db.models import Count
register = template.Library()

@register.inclusion_tag('left_content.html')
def myInclusion(username):
    user = models.UserInfo.objects.filter(username=username)[0]
    blog = user.blog
    category_list = models.Category.objects.filter(blog=blog).annotate(num=Count("article")).values('title', 'num')
    tag_list = models.Tag.objects.filter(blog=blog).annotate(num=Count("article")).values('title', 'num')
    archive_list = models.Article.objects.filter(user=user).extra(
        select={'article_time': "date_format(create_time,'%%Y-%%m')"}).values('article_time').annotate(
        num=Count("pk")).values('article_time', 'num')
    return {'category_list':category_list,
            'tag_list':tag_list,
             'archive_list':archive_list,
            'user':user}



