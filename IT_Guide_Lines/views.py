from django.shortcuts import render
from .models import SoftwareEngineer
from .models import DataEngineer
from .models import SecurityEngineer
from .models import GameEngineer

# Create your views here.


def home(request):
    """The homepage """
    return render(request,'home.html')

def software_engineer_list(request):
    engineers = SoftwareEngineer.objects.all()
    context = {'engineers': engineers}
    return render(request, 'templates/software.html', context)


def data_engineer_list(request):
    data_engineers = DataEngineer.objects.all()
    context = {'data_engineers': data_engineers}
    return render(request, 'data_engineer.html', context)


def security_engineer_list(request):
    security_engineers = SecurityEngineer.objects.all()
    context = {'security_engineers': security_engineers}
    return render(request, 'security_engineer.html', context)



def game_engineer_list(request):
    game_engineers = GameEngineer.objects.all()
    context = {'game_engineers': game_engineers}
    return render(request, 'game_engineert.html', context)