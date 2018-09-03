from django.shortcuts import render
from django.http import HttpResponse
import json

# Create your views here.


def index(request):
    with open('song.json') as f:
        data = json.load(f)
        artist = data['artists'][0]['name']
        song_name = data['name']
    with open('user.json') as u:
        user = json.load(u)
    html = "<html><body><h1>%s dinliyor %s-%s</h2></body></html>" % (
        user, artist, song_name)
    return HttpResponse(html)
