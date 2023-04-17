from django.urls import path
from . import views

app_name= 'career_webs'
urlpatterns = [
    #Home page
    path('', views.index, name='index'),
    path('softwares/', views.softwares, name='softwares'),
    path('softwares/<int:software_id>', views.software, name='software'),
]