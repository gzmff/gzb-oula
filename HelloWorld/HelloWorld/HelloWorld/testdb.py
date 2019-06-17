# -*- coding: utf-8 -*-

from django.http import HttpResponse

from TestModel.models import Test
from TestModel.models import weathers
from TestModel.models import phone
from TestModel.models import movie 

from django.shortcuts import render
import MySQLdb

#数据库操作
def testdb(request):
    '''response = ""
    response1 = ""
    '''
    allList = Test.objects.all()#获取top250电影
    weather = weathers.objects.all()#获取天气
    phones = phone.objects.all()#获取手机信息
    movies = movie.objects.all()#获取美剧
    # meiju = meiju.objects.all()

    '''response3 = Test.objects.get(id=1)'''

    '''Test.objects.order_by('name')[0:2]'''

    Test.objects.order_by("id")

    '''Test.objects.filter(name="runoob").order_by("id")'''

    '''for var in list:
        response1 += var.content + " "
    response = response1
    return HttpResponse("<p>" + response + "</p>")
    context          = {}
    context['top250'] = response'''
    return render(request,'base.html',{'allList':allList,'weather':weather,'phones':phones,'movies':movies})
       


