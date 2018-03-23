from django.http import *
from django.shortcuts import render



# Create your views here.
def set_session(request):

    request.session['username'] = 'qiong'
    request.session['verify_code'] = 'yuyu'

    response = HttpResponse('保存session成功')

    response.set_cookie('username','qiongqiong')

    response.set_cookie('password','89898989')


    return response


def get_session(request):

    username = request.session['username']
    verify_code = request.session['verify_code']

    cookies_user = request.COOKIES['username']
    cookies_pass = request.COOKIES['password']

    text = 'session :\n username = %s \n verify_code = %s' %(username,verify_code)+'cookies:\nusername = %s \n verify_code = %s'%(cookies_user,cookies_pass)


    return HttpResponse(text)


def buy_car(request):



    return render(request , 'buy_car.html')


def submit_car(request):

    goods_1 = request.GET.get('goods_1')
    number = request.GET.get('num')
    print(goods_1,number)

    return HttpResponse('数据已收到')