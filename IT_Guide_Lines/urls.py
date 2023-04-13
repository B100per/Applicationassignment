from IT_Guide_Lines.views import (
    software_engineer_list,
    data_engineer_list,
    security_engineer_list,
    game_engineer_list,
    home
)
from django.urls import path
app_name = 'Doc'

urlpatterns = [
    path('', home, name='home'),
    path('engineers/', software_engineer_list, name='engineer_list'),
    path('data_engineers/', data_engineer_list, name='data_engineer_list'),
    path('security_engineers/', security_engineer_list, name='security_engineer_list'),
    path('game_engineers/', game_engineer_list, name='game_engineer_list'),
]
