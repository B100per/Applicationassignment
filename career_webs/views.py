from django.shortcuts import render
from .models import Software

# Create your views here.
def index(request):
    """The home page of career webs"""
    return render(request, 'career_webs/index.html')

def softwares(request):
    softwares = Software.objects.order_by('date_added')
    context = {'softwares': softwares}
    return render(request, 'career_webs/softwares.html', context)

def software(request, software_id):
    software = Software.objects.get(id=software_id)
    skills = software.skill_set.order_by('-date_added')
    context = {'software': software,'skills':skills}
    return render(request, 'career_webs/software.html', context)