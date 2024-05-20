from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_page),
    path('age/',views.calc_age, name='calc_age')
]