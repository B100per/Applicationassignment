from django import forms
from .models import SoftwareEngineer,DataEngineer,SecurityEngineer,GameEngineer

class SoftwareEngineerForm(forms.ModelForm):
    class Meta:
        model = SoftwareEngineer
        fields = ('name', 'skills', 'information')
        
class DataEngineerForm(forms.ModelForm):
    class Meta:
        model = DataEngineer
        fields = ('name', 'skills', 'information')

class SecurityEngineerForm(forms.ModelForm):
    class Meta:
        model = SecurityEngineer
        fields = ('name', 'skills', 'information')

class GameEngineerForm(forms.ModelForm):
    class Meta:
        model = GameEngineer
        fields = ('name', 'skills', 'information')