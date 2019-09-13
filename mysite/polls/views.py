# from django.shortcuts import render

# Create your views here.
# from django.http import HttpResponse


# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")

from polls.models import Music
from polls.serializers import MusicSerializer
from rest_framework import generics
class MusicListCreate(generics.ListCreateAPIView):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer
