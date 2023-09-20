
from django.urls import path
from . import views

urlpatterns = [
    path('', views.homePage, name='home'),
    path('analyze/', views.personalityPage, name='analyse'),
    path('trends/', views.trendsPage, name='trends'),
    path('<str:user>/', views.UserPage, name='user'),
    path('about/', views.about_us, name='about-us'),
    path('contact/', views.contact_us, name='contact-us'),
]
