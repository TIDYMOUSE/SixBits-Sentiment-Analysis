from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.db.models import Q

# Create your views here.

# return render(request, 'app-name/filename.html')
# where app-name are personality, posts, trends and core. dont forget to remove old return statement

TRENDS = {trend.post_trend for trend in Post.objects.all()}


def homePage(request):
    return render(request, "core/intro_page.html")


def personalityPage(request):
    return render(request, "posts/analyse.html")


def UserPage(request, user):

    posts = Post.objects.filter(Q(username__contains=user))
    context = {
        "posts": posts,
        "username": user,
        "trends": TRENDS,
    }
    return render(request, "personality/UserPage.html", context)


def trendsPage(request):

    q = request.GET.get("q") if request.GET.get("q") != None else ''

    post = Post.objects.all()

    context = {
        "posts": post,
        "trends": TRENDS,
    }

    return render(request, "trends/posts.html", context)


def about_us(request):
    return render(request, 'core/About.html')


def contact_us(request):
    return render(request, 'core/contact_us.html')
