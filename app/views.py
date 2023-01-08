from datetime import datetime, timedelta

from django.shortcuts import render

# Create your views here.
def setcookies(request):
    response = render(request, 'setcookies.html')
    #response.set_cookie('age', '20')
    #response.set_cookie('age', '20', max_age=20)
    response.set_cookie('age', '20', expires=datetime.utcnow() + timedelta(days=1))
    return response


def getcookies(request):
    cookies = request.COOKIES.get('age')
    return render(request, 'getcookies.html', {'cookies': cookies})

def delcookies(request):
    response = render(request, 'delcookies.html')
    response.delete_cookie('age')
    return response
