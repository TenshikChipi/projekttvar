from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.aboutus),
    path('colortp',views.colortp),
    path('colottypetest',views.colottypetest), 
    path('log',views.log),
    path('menu',views.menu),
    path('otcek',views.otcek),
    path('sig',views.sign),
    path('spring',views.spring),
    path('summer',views.summer),
    path('wardrob',views.wardrob),
    path('winter',views.winter),
    path('autumn',views.autumn),
    path('avtorization',views.avtorization),
    path('index',views.index),
    path('myoutfits',views.my_outfits),
    path('registr',views.registr),
    path('workshop',views.workshop),
]