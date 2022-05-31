from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return HttpResponse("hello world")

def demo1(request):
    #return HttpResponse("<h1>my name is demo</h1>")
    return render(request,'home.html',{'name':'ayush'})


def add1(request):
    var1= int(request.POST["num1"])
    var2= int(request.POST["num2"])
    res=var1+var2
    return render(request,'result.html',{'result':res})
