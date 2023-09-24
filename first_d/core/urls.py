from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sub_url/', views.sub_url, name='sub_url')
]
