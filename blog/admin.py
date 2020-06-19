from django.contrib import admin
from blog import models
# Register your models here.


admin.site.register(models.UserInfo)
# print(admin.site._registry,end='\n')
admin.site.register(models.Blog)
admin.site.register(models.Category)
admin.site.register(models.Tag)
admin.site.register(models.Article)
admin.site.register(models.ArticleDetail)
admin.site.register(models.Article2Tag)
admin.site.register(models.ArticleUpDown)
admin.site.register(models.Comment)

# print(admin.site._registry)