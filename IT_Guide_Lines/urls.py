from .import views
from django.urls import path
app_name = 'IT_Guide_Lines'

urlpatterns = [
    path('', views.home, name='home'),
    path('software_engineer_list/', views.software_engineer_list, name='software_engineer_list'),
    path('data_engineer_list/', views.data_engineer_list, name='data_engineer_list'),
    path('security_engineer_list/', views.security_engineer_list, name='security_engineer_list'),
    path('game_engineer_list/', views.game_engineer_list, name='game_engineer_list'),
]
