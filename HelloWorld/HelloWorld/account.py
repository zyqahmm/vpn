from django.shortcuts import render

def index(request):
    account={}
    account={
        "server":"104.153.100.121",
        "server_port":443,
        "password":"redhat",
        "method":"aes-256-cfb"
    }
    return render(request,'account.html',account)