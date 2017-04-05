from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from . import models


def helloTemplates(request):
    context = {}
    context['hello'] = 'Hello templates!'
    return render_to_response("../templates/hello.html", context)


def helloModel(request):
    # testmodel = models.Hotel(name="单人房", cf=20, br=15)
    # testmodel.save()
    testModels = models.Hotel.objects.all()
    json_data = serializers.serialize("json", testModels)
    return HttpResponse(json_data, content_type="application/json")


'''




 Person.objects.all() # 查询所有
Person.objects.all()[:10] 切片操作，获取10个人，不支持负索引，切片可以节约内存，不支持负索引，后面有相应解决办法，第7条
Person.objects.get(name="WeizhongTu") # 名称为 WeizhongTu 的一条，多条会报错

get是用来获取一个对象的，如果需要获取满足条件的一些人，就要用到filter
Person.objects.filter(name="abc") # 等于Person.objects.filter(name__exact="abc") 名称严格等于 "abc" 的人
Person.objects.filter(name__iexact="abc") # 名称为 abc 但是不区分大小写，可以找到 ABC, Abc, aBC，这些都符合条件

Person.objects.filter(name__contains="abc") # 名称中包含 "abc"的人
Person.objects.filter(name__icontains="abc") #名称中包含 "abc"，且abc不区分大小写

Person.objects.filter(name__regex="^abc") # 正则表达式查询
Person.objects.filter(name__iregex="^abc")# 正则表达式不区分大小写

# filter是找出满足条件的，当然也有排除符合某条件的
Person.objects.exclude(name__contains="WZ") # 排除包含 WZ 的Person对象
Person.objects.filter(name__contains="abc").exclude(age=23) # 找出名称含有abc, 但是排除年龄是23岁的
 '''


def helloWorld(request):
    return HttpResponse("Hello world ! ")


def helloJson1(request):
    json_data = [{'name': 'zhangsan', 'age': 30}]
    return HttpResponse(json_data, content_type="application/json")


def helloJson2(request):
    modelhello = models.Student("zhangsan", 20)
    return HttpResponse([modelhello.__dict__], content_type="application/json")


def helloParam1(request, param):
    return HttpResponse("param: " + param)


def helloParam2(request, param1, param2):
    return HttpResponse("param1 = " + param1 + "   <br>param2 = " + param2)


def helloParam3(request, param1, param2):
    return HttpResponse("param1 = " + param1 + "   <br>param2 = " + param2)


def helloParam4(request):
    p1 = request.GET.get('p1')
    p2 = request.GET.get('p2')
    return HttpResponse("p1 = " + p1 + "   <br>p2 = " + p2)


@csrf_exempt
def helloParam5(request):
    # p1 = request.POST.get('p1')
    # p2 = request.POST.get('p2')
    if request.POST:
        paramObj = request.POST
        print(paramObj)
        lists = paramObj.getlist(' name')
        a= lists[0]
        print(lists[0])
        print(lists[1])
    return HttpResponse("ok")
