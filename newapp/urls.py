from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.indexpage,name="index"),
    path('sports', views.sports, name="sports"),
    path('business', views.business),
    path('politics', views.politics, name="politics"),
    path('science', views.science, name="science"),
    path('entertainment', views.entertainment, name="entertainment"),
    path('Automobile', views.Automobile, name="Automobile"),

]