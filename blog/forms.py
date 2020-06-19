#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "wls"
# Date: 2019/10/21

'''
form表单相关的
'''

from django import forms
from django.forms import widgets
from django.core.exceptions import ValidationError
from blog import models
class RegForm(forms.Form):
    username = forms.CharField(
        #校验规则
        max_length=16,
        label='用户名',
        error_messages={
            'max_length': '用户名不能超过16位',
            'required': '不能为空'
        },
        #生成HTML代码由widget控制,生成TextInput框,有这个类
        widget=widgets.TextInput(attrs={'class':'form-control'}),

    )

    password = forms.CharField(
        min_length=6,
        label='密码',
        widget=widgets.PasswordInput(attrs={'class':'form-control'},render_value=True),
        error_messages={
            'min_length': '密码至少6位',
            'required': '不能为空'
        }
    )

    re_password = forms.CharField(
        min_length=6,
        label='确认密码',
        widget=widgets.PasswordInput(attrs={'class':'form-control'},render_value=True),
        error_messages={
            'min_length': '密码至少6位',
            'required': '不能为空'
        }
    )
    email = forms.EmailField(
        label='邮箱',
        widget=widgets.EmailInput(attrs={'class':'form-control'}),
        error_messages={
            'required':'不能为空',
            'invalid':'邮箱格式不正确'
        }
    )




    def clean_username(self):
        username = self.cleaned_data.get('username')
        r = models.UserInfo.objects.filter(username=username)
        if r:
            self.add_error('username',ValidationError("用户名已经存在"))
        else:
            return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        r = models.UserInfo.objects.filter(email=email)
        if r:
            self.add_error('email',ValidationError("邮箱已经存在"))
        else:
            return email

    def clean(self):
        password = self.cleaned_data.get('password')
        re_password = self.cleaned_data.get('re_password')
        if password and password!=re_password:
            self.add_error('re_password',ValidationError('两次密码不一致'))
            raise ValidationError('两次密码不一致')
        else:
            return self.cleaned_data