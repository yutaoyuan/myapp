from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('reputation-tags/', views.reputation_tags, name='reputation_tags'),
    path('reputation-log/', views.reputation_log, name='reputation_log'),
]
