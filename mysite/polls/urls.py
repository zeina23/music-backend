# from django.urls import path

# from . import views

# urlpatterns = [
#     path('', views.index, name='index'),
# ]

from django.urls import path
from . import views
urlpatterns = [
    path('api/mysite/', views.MusicListCreate.as_view() ),
]
