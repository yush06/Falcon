from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth  #import this lline

# Create your views here.

def register(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                print('Username taken')
            elif User.objects.filter(email=email).exists():
                print('email taken')
            else:
                user=User.objects.create_user(username=username,email=email,password=password1,first_name=first_name,last_name=last_name)
                user.save();
                print('user created')
        else:
            print('Password not matching ')
        #return render(request,'index.html')
        return redirect('/')
    else:
         return render(request,'register.html')
