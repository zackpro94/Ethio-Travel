from django import urls
from django.urls import path
from . import views
app_name = 'ethiotravel'

urlpatterns = [
    path('', views.index, name='index'),
    path('about.html', views.about, name='about'),
    path('news.html', views.news, name='news'),
    path('contact.html', views.contact, name='contact'),
    path('<slug:post>/', views.dest_detail, name='dest_detail'),
]
