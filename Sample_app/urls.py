from django.contrib import admin
from django.urls import path
from Sample_app import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name="about"),
    path('product', views.product, name="product"),
    path('contact', views.contact, name="contact"),
    path('team', views.team, name="team"),
    path('visit', views.visit, name="visit"),
    path('login', views.login, name='login'),
    path('project', views.project, name='project'),
]