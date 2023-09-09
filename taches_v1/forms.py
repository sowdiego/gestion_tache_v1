from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from .models import Tache, FilterTache

UserModel = get_user_model()


class UserRegistrationForm(UserCreationForm):

    class Meta:
        model = UserModel
        fields = ["username", "password1", "password2"]

class UpdateTacheForm(forms.ModelForm):  
    class Meta:  
        model = Tache  
        fields = ['titre','date_creation', 'date_echeance', 'description', 'statut']
        labels = {
            'titre': "Le titre",
            'date_creation': "La date de création",
            'date_echeance': "La date d'échéance",
            'description': "La description",
            'statut': "Terminée",
        }
class DateInput(forms.DateTimeInput):
    input_type = 'date'

class CreateTacheForm(forms.ModelForm):  
    class Meta:  
        model = Tache
        model.date_creation = forms.DateField(widget=DateInput)
        
        fields = ['titre', 'date_echeance', 'date_creation', 'description']
        labels = {
            'titre': "Le titre",
            'date_creation': "La date de création",
            'date_echeance': "La date d'échéance",
            'description': "La description",
        }

class FilterTacheForm(forms.ModelForm):  
    class Meta:  
        model = FilterTache
        fields = ['est_terminer', 'date_debut', 'date_fin']
        labels = {
            'est_terminer': "Les taches terminées",
            'date_debut': "Date début",
            'date_fin': "Date fin"
           
        }
       
        