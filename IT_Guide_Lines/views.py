from django.shortcuts import render
from .models import SoftwareEngineer
from .models import DataEngineer
from .models import SecurityEngineer
from .models import GameEngineer

# Create your views here.


def home(request):
    """The homepage """
    return render(request,'IT-templates/home.html')

def software_engineer_list(request):
    engineers = SoftwareEngineer.objects.all()
    context = {'engineers': engineers}
    return render(request, 'IT-templates/software.html', context)


def data_engineer_list(request):
    data_engineers = DataEngineer.objects.all()
    context = {'data_engineers': data_engineers}
    return render(request, 'IT-templates/data_engineer.html', context)


def security_engineer_list(request):
    security_engineers = SecurityEngineer.objects.all()
    context = {'security_engineers': security_engineers}
    return render(request, 'IT-templates/security_engineer.html', context)



def game_engineer_list(request):
    game_engineers = GameEngineer.objects.all()
    context = {'game_engineers': game_engineers}
    return render(request, 'IT-templates/game_engineer.html', context)
