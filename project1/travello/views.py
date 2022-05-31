from django.shortcuts import render
from . models import Destination
# Create your views here.
def index(request):
    de=Destination.objects.all()
    #return HttpResponse("<h1>my name is demo</h1>")
    return render(request,'index.html',{'dest':de})

