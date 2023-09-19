from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.

# return render(request, 'app-name/filename.html')
# where app-name are personality, posts, trends and core. dont forget to remove old return statement

TRENDS = {trend.post_trend for trend in Post.objects.all()}


def homePage(request):
    return render(request, "core/intro_page.html")


def personalityPage(request):
    return render(request, "core/analyze.html")


def postsPage(request):
    return HttpResponse("This is personality page")


def trendsPage(request):

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
