from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('npc_list/', views.npc_list, name='npc_list'),
    path('npc_list/npc/<str:npc_name>/', views.npc_name, name='npc_name'),
    re_path(r'npc_list/birth/(?P<year>[0-9]{4})/$', views.birth_year, name='birth'),
]
