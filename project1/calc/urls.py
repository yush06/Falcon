from django.urls import path
from . import views

urlpatterns=[ path('',views.home,name='home'),
    path('demo1',views.demo1,name='demo1'),
    path('add1',views.add1,name='add1'),

]