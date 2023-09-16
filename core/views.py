from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# return render(request, 'app-name/filename.html')
# where app-name are personality, posts, trends and core. dont forget to remove old return statement


def homePage(request):
    return HttpResponse("This is home page")


def personalityPage(request):
    return HttpResponse("This is personality page")


def postsPage(request):
    return HttpResponse("This is personality page")


def trendsPage(request):
    return HttpResponse("This is personality page")
