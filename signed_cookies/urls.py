
from django.urls import path
from . import views

urlpatterns = [
    path('set/', views.setcookies, name='setcookies'),
    path('del/', views.delcookies),
    path('get/', views.getcookies)
    ]
