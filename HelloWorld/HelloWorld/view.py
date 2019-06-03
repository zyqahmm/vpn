from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render_to_response
from userinfo.models import userinfo
import os

MailCode="123"


def hello(request):
    return HttpResponse("Hi Michael")

def hi(request):
    context={}
    context['hello'] = 'Hi Michael'
    return render(request,'hello.html',context)

def login(request):
    return render_to_response('login.html')

def veritify(request):
    request.encoding='utf-8'
    response = ""
    list = userinfo.objects.all()
    for var in list:
        if var.Mail == request.GET["Mail"]:
            account={}
            account={
                "server":"104.153.100.121",
                "server_port":443,
                "password":"redhat",
                "method":"aes-256-cfb"
            }
            return render(request,'account.html',account)
            break
        else:
            return render(request,"regist.html")

def regist(request):
    Mail = request.GET["Mail"]
    Phone = request.GET["Phone"]
    TITLE="VPN_verification_code"
    sendmail="echo " + MailCode + "| mail -s "  + TITLE + " "+ Mail
    fo=open("/tmp/test.txt","w")
    fo.write(sendmail)
    fo.close()
    insert=userinfo(Mail,Phone)
    insert.save()
#    os.system(sendmail)
    return render(request,"code.html")


def code(request):
    Code=request.GET['Code']
    if Code==MailCode:
        return render(request,"login.html")
    else:
        return HttpResponse("code error,please try again!")

def insert(request):
    insert = userinfo(Mail='1628575993@qq.com',Phone='12345678901')
    insert.save()
    return HttpResponse("insert into db success")


def search(request):
    response = ""
    response1 = ""
    list = userinfo.objects.all()
    response = userinfo.objects.filter(id=1)
    for var in list:
        response1 += var.Mail
    response = response1
    return HttpResponse(response)
    