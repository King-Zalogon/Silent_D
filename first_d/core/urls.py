from django.urls import path, re_path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # path('accounts/', include('django.contrib.auth.urls'))
    path('accounts/login', auth_views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('accounts/logout', auth_views.LogoutView.as_view(), name='logout'),
    path('', views.index, name='index'),
    path('char_form', views.contact, name="char_form"),
    path('npc_list/', views.npc_list, name='npc_list'),
    path('npc_list/<str:npc_name>/', views.npc_name, name='npc_name'),
    re_path(r'npc_list/birth/(?P<year>[0-9]{4})/$', views.birth_year, name='birth'),
    path('rules_systems_form', views.RulesSystemCreateView.as_view(), name="rules_systems_form"),
    path('rules_systems_list', views.RulesSystemListView.as_view(), name='rules_systems_list')

]
