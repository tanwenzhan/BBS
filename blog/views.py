from django.shortcuts import render,HttpResponse,redirect
from blog import models
from django.contrib import auth
from django.http import JsonResponse
from blog import forms
from geetest import GeetestLib
import json
from django.db.models import Count,F
# Create your views here.

#登陆视图
def login(request):
    if request.method=='POST':
        ret = {"status": 0, "msg": ""}
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(111)
        gt = GeetestLib(pc_geetest_id, pc_geetest_key)
        challenge = request.POST.get(gt.FN_CHALLENGE, '')
        validate = request.POST.get(gt.FN_VALIDATE, '')
        seccode = request.POST.get(gt.FN_SECCODE, '')
        status = request.session[gt.GT_STATUS_SESSION_KEY]
        user_id = request.session["user_id"]
        if status:
            result = gt.success_validate(challenge, validate, seccode, user_id)
        else:
            result = gt.failback_validate(challenge, validate, seccode)
        if result:
            # 验证码正确
            # 利用auth模块做用户名和密码的校验
            user = auth.authenticate(username=username, password=password)
            if user:
                # 用户名密码正确
                # 给用户做登录
                auth.login(request, user)
                ret["msg"] = "/index/"
            else:
                # 用户名密码错误
                ret["status"] = 1
                ret["msg"] = "用户名或密码错误！"
        else:
            ret["status"] = 1
            ret["msg"] = "验证码错误"
        return JsonResponse(ret)
    return render(request,'login.html')

#注销视图
def logout(request):
    auth.logout(request)
    return redirect('/index/')
#blog的主页视图
def index(request):
    article_list = models.Article.objects.all()
    return render(request,'index.html',{'article_list':article_list})


#获取滑动验证码的url

pc_geetest_id = "b46d1900d0a894591916ea94ea91bd2c"
pc_geetest_key = "36fc3fe98530eea08dfc6ce76e3d24c4"
def get_geetest(request):
    user_id = 'test'
    gt = GeetestLib(pc_geetest_id, pc_geetest_key)
    status = gt.pre_process(user_id)
    request.session[gt.GT_STATUS_SESSION_KEY] = status
    request.session["user_id"] = user_id
    response_str = gt.get_response_str()
    return HttpResponse(response_str)



#注册视图函数
def register(request):
    if request.method=='POST':
        ret={"status":0,"msg":""}
        forms_obj = forms.RegForm(request.POST)
        if forms_obj.is_valid():
            forms_obj.cleaned_data.pop('re_password')
            avatar_img=request.FILES.get('avatar')
            models.UserInfo.objects.create_user(**forms_obj.cleaned_data,avatar=avatar_img)
            ret["msg"]='/login/'
            return JsonResponse(ret)
        else:
            ret["status"]=1
            ret["msg"]=forms_obj.errors
            return JsonResponse(ret)

    forms_obj = forms.RegForm()
    return render(request,'register.html',{'forms_obj':forms_obj})

#检测用户名是否存在
def check_username_exits(request):
    ret = {"status":0,"msg":""}
    username = request.GET.get('username')
    is_exits = models.UserInfo.objects.filter(username=username)
    if is_exits:
        ret["status"]=1
        ret["msg"]="用户名已经被注册"
        return JsonResponse(ret)
    else:
        return JsonResponse(ret)

#个人博客主页的视图
def home(request,username):
    user = models.UserInfo.objects.filter(username=username)[0]
    article_list = user.article_set.all()
    blog = user.blog
    return render(request,'home.html',{'blog':blog,'user':user,
                                       'article_list':article_list,
                                       'username':username})
#文章详情表
def article_detail(request,username,pk):
    comment_list = models.Comment.objects.filter(article_id=pk)
    article_obj = models.Article.objects.filter(pk=pk).first()
    return render(request,'article_detail.html',{'article_obj':article_obj,
                                                 'username':username,
                                                 'comment_list':comment_list
                                                 })

#文章分类跳转视图
def category_url_handle(request,username,title):
    user = models.UserInfo.objects.filter(username=username).first()
    category_article= models.Category.objects.filter(title=title).first()
    category_article_list =models.Article.objects.filter(category=category_article,user=user)
    return render(request,'category_article_list.html',{
        'username':username,
        'article_list':category_article_list
    })
#标签分类跳转视图
def tag_url_handle(request,username,title):
    user = models.UserInfo.objects.filter(username=username).first()
    tag_article= models.Tag.objects.filter(title=title).first()
    tage_article_list =models.Article.objects.filter(tags=tag_article,user=user)
    return render(request,'category_article_list.html',{
        'username':username,
        'article_list':tage_article_list
    })
#时间归档跳转视图
def archive_url_handle(request,username,create_time):
    ret =models.Article.objects.extra(select={'sql_time': "date_format(create_time,'%%Y-%%m')"}).values("sql_time",'nid')
    ii=[]
    for i in ret:
        if i['sql_time']==create_time:
            ii.append(i['nid'])
    user=models.UserInfo.objects.filter(username=username).first()

    archive_article_list=models.Article.objects.filter(nid__in=ii,user=user)
    return render(request,'category_article_list.html',{
        'username':username,
        'article_list':archive_article_list

    })


#文章点赞与踩的视图
def up_down(request):
    user=request.user
    is_up = request.POST.get('is_up')
    is_up = json.loads(is_up)
    article_id = request.POST.get('article_id')[0]
    ret = {"status":0}
    try:
        # print('查看是否报错')
        models.ArticleUpDown.objects.create(user=user,article_id=article_id,is_up=is_up)
        article = models.Article.objects.filter(nid=article_id)
        if is_up:
            article.update(up_count=F("up_count")+1)
        else:
            article.update(down_count=F("down_count") + 1)
    except Exception as e:
        # print('报错了')
        ret["status"]=1
        up_down_obj = models.ArticleUpDown.objects.filter(user=user, article_id=article_id).first()
        ret['fisrt_action']=up_down_obj.is_up
    return JsonResponse(ret)

#分类三和一的视图
# def three_on(request):


#评论的视图
def comment(request,article_id):
    print(request.POST)
    user = request.user
    comment_content = request.POST.get('comment_content')
    pid = request.POST.get('pid')
    # print(pid)
    if not pid:
        comment_obj = models.Comment.objects.create(content=comment_content,article_id=article_id,user_id=user.nid)
    else:
        comment_obj = models.Comment.objects.create(content=comment_content,article_id=article_id,user_id=user.nid,parent_comment_id=pid)
    from django.db.models import F
    models.Article.objects.update(comment_count=F('comment_count')+1)

    response  = {}
    response['create_time'] = comment_obj.create_time.strftime('%Y-%m-%d %H:%M:%S')
    response['content'] = comment_obj.content
    response['username'] = request.user.username
    # print(response['create_time'])
    return JsonResponse(response)


def comment_tree(request,pk):
    all_comment = models.Comment.objects.filter(article_id=pk).values('nid','content','parent_comment_id')
    all_comment = list(all_comment)
    print(all_comment)
    return JsonResponse(all_comment,safe=False)
from bs4 import BeautifulSoup
#文章添加
def addarticle(request):
    if request.method=='POST':
        user = request.user
        article_content = request.POST.get('article_content')
        print(article_content)
        title = request.POST.get('title')
        soup = BeautifulSoup(article_content,'html.parser')
        desc = soup.text[0:150]
        ret = soup.find_all()
        for tag in ret:
            if tag.name=='script':
                # print(tag.name)
                tag.decompose()
        # print(str(soup))
        article_obj = models.Article.objects.create(user=user,title=title,desc=desc)
        models.ArticleDetail.objects.create(content=str(soup),article=article_obj)
        return redirect('/index/')
    return render(request,'add_article.html')
#图片上传
def upload(request):
    # print(request.FILES)
    file_obj = request.FILES.get('upname')
    from bbs import settings
    import os,json
    path = os.path.join(settings.MEDIA_ROOT,'add_article_img',file_obj.name)
    with open(path,'wb')as f :
        for i in file_obj.chunks():
            f.write(i)
    import time
    time.sleep(2)
    ret = {
        "error":0,
        "url":"/media/add_article_img/"+file_obj.name
    }
    return HttpResponse(json.dumps(ret))



#编辑文章
def edit_article(request,article_pk):
    if request.method=="POST":
        article_content = request.POST.get('article_content')
        title = request.POST.get('title')
        soup = BeautifulSoup(article_content,'html.parser')
        ret = soup.find_all()
        for tag in ret:
            if tag in ['script', 'link']:
                tag.decompose()
        desc = soup.text[0:150]
        # print('desc',desc)
        article_obj = models.Article.objects.filter(pk=article_pk)
        article_obj.update(title=title,desc=desc)

        content=str(soup)
        # print('content',content)
        models.ArticleDetail.objects.filter(article=article_obj).update(content=content)
        url='/blog/{}/article/{}/'.format(request.user.username,article_pk)
        return redirect(url)
    article_obj = models.Article.objects.filter(pk=article_pk)[0]
    return render(request,'edit_article.html',{'article_obj':article_obj})

#删除文章
def delete_article(request,pk):
    try:
        article_obj = models.Article.objects.filter(pk=pk).first()
        article_obj.delete()
        pik = article_obj.pk
        models.ArticleDetail.objects.filter(article_id=pik).first().delete()

        # print('删除成功')
    except Exception as e:
        pass
    return redirect('/index/')