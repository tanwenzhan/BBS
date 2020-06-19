#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "wls"
# Date: 2019/10/22

import os
if __name__ == '__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bbs.settings")
    import django
    django.setup()
    from blog import models

    # print(models.UserInfo.objects,type(models.UserInfo.objects))
    # print(models.UserInfo.objects.all(),type(models.UserInfo.objects.all()))
    # print(models.UserInfo.objects.first().nid)
    # print(models.UserInfo.objects.filter(nid=12).values('article__title'))
    # print(models.Article.objects.first().user.username)
    # print(models.Article.objects.first().nid)
    # print(models.Article.objects.filter(nid=1).values('user__username'))
    # print(models.UserInfo.objects.first().article_set)
    # print(models.UserInfo.objects.filter(username='xiaohei')[0].nid)
    # print(models.UserInfo.objects.first().article_set.all()[0].title)
    # print(models.UserInfo.objects.filter(nid=12).values('article__title')[0])
    user = models.UserInfo.objects.first()
    blog=user.blog
    # print(blog.title)
    from django.db.models import Count
    # ret= models.Category.objects.filter(blog=blog).annotate(a=Count("article")).values('a','title',)
    # print(ret)
    # ret= models.Category.objects.filter(blog=blog).annotate(a=Count("article"))
    # print(ret)
    # for i in ret:
    #     print(i,i.a,)
    # ret = models.Article.objects.extra(select={'article_time':"date_format(create_time,'%%Y-%%m')"}).\
    # ret = models.Article.objects.filter(user=user).extra(select={'article_time':"date_format(create_time,'%%Y-%%m')"}).values('article_time').annotate(c=Count("pk")).values('article_time','c')
    # print(ret)
    # ret = models.Article.objects.extra(select={'c':"date_format(create_time,'%%Y-%%m-%%d %%H:%%i:%%s')"}).values('c')
    # print(ret)
    # ret = models.Category.objects.filter(title='技术').first()
    # print(models.Category.objects.filter(title='技术')[0].article_set.all())
    # print(type(models.Category.objects.filter(title='技术').values_list('article').first()[0]))
    # for i in ret:
    #     print(i)
    #     print(i['title'])
    # s = models.Article.objects.filter(category=ret)
    #
    # print(s)
    # for i in s:
    #     print(i.title)'2019-02'
    # ret = models.Category.objects.filter(title='NBA').values("blog__userinfo__username").first()
    # print(ret['blog__userinfo__username'])
    # ret = models.Article.objects.extra(select={'sql_time': "date_format(create_time,'%%Y-%%m')"}).values("sql_time",
    #                                                                                                      'nid')
    # ii = []
    # for i in ret:
    #     if i['sql_time'] == '2019-02':
    #         ii.append(i['nid'])
    #
    # archive_article_list = models.Article.objects.filter(nid__in=ii)
    # print(archive_article_list)
    # ret = models.UserInfo.objects.first()
    # print(ret,type(ret))
    # ret = models.UserInfo.objects.filter(nid='12')
    # print(ret)
    # re1t = models.UserInfo.objects.filter(nid=12)
    # print(re1t)
    # print(ret,type(ret))
    # import json
    # # ret = models.UserInfo.objects.filter(nid=12).first()
    # ret =list(models.UserInfo.objects.filter(nid=12).values_list('username','password'))
    # ret = json.dumps(ret)
    # print(ret)
    # ret = models.Article.objects.filter(pk=19).update(title='又一次更新操作',desc='又一次更新操作又一次更新操作又一次更新操作又一次更新操作又一次更新操作')
    # print(ret,type(ret))


