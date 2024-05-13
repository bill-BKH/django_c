from django.shortcuts import render
from django.http import HttpResponse
from .models import Music
# Create your views here.
def home(request):
    all_music = Music.objects.all()
    return render(request, 'music/index.html', {'musics':all_music})


def gamgin(request):
    all_music = Music.objects.filter(genres='gamgin')
    return render(request, 'music/index_gamgin.html', {'musics':all_music})
