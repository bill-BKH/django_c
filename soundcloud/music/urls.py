from . import views
from django.urls import path

app_name = 'music'

urlpatterns = [
    path('', views.home, name='home'),
    path('gamgin/', views.gamgin, name='gamgin'),
    path('shad/',views.shad,name='shad'),
    path("classic",views.classic,name='classic'),
    path('pop/',views.pop, name='pop'),
    path('rap/',views.rap,name='rap'),
     path('rock/',views.rap,name='rock'),
]