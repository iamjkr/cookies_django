from datetime import datetime, timedelta

from django.shortcuts import render

# Create your views here.
def setcookies(request):
    response = render(request, 'singned_cookies/setcookies.html')
    #response.set_cookie('age', '20')
    response.set_signed_cookie('age', '20', salt= 'nm', max_age=20)
    #response.set_signed_cookie('age', '20', expires=datetime.utcnow() + timedelta(days=1))
    return response


def getcookies(request):
    #salt name should be same else error, we cab set default to avoid exception
    cookies = request.get_signed_cookie('age',default='Guest', salt= 'nmm')
    return render(request, 'singned_cookies/getcookies.html', {'cookies': cookies})

def delcookies(request):
    response = render(request, 'singned_cookies/delcookies.html')
    response.delete_cookie('age')
    return response
