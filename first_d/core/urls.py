from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sub_url/', views.sub_url, name='sub_url'),
    path('sub_url/npc/<str:npc_name>/', views.npc_name, name='npc_name'),
    re_path(r'sub_url/birth/(?P<year>[0-9]{4})/$', views.birth_year, name='birth'),
]
