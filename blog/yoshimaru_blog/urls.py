from django.urls import path
from . import views

app_name = 'yoshimaru_blog'
urlpatterns = [
  path('', views.index, name='index')
]
