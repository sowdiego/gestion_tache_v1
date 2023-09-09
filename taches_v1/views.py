import gettext
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import Tache
from .forms import CreateTacheForm, UpdateTacheForm, FilterTacheForm
from django.shortcuts import (get_object_or_404,
                              render,
                              HttpResponseRedirect)
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages    
from django.core.paginator import Paginator


# view pour l'authentification

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/login')
    else:
        form = UserCreationForm()
    return render(request, 'taches_v1/signup.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('/login')

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            # messages.success(request, gettext("Login successfully !"))
            return redirect('acceuil')
    else:
        form = AuthenticationForm()
    return render(request, 'taches_v1/login.html', {'form': form})

# wiews pour la gestion des taches

@csrf_protect
@login_required(login_url='/login')
def acceuil(request):
    mes_taches = Tache.objects.all()
    page_number = request.GET.get('page') 
    paginator = Paginator(mes_taches, 5) 
    page = paginator.get_page(page_number) 
    form = FilterTacheForm(request.POST or None)
    if form.is_valid():
        est_terminer = form.cleaned_data.get('est_terminer')
        date_debut = form.cleaned_data.get('date_debut')
        date_fin = form.cleaned_data.get('date_fin')
        if est_terminer:
            mes_taches = mes_taches.filter(statut = est_terminer)
        if date_debut:
            mes_taches = mes_taches.filter(date_creation__gte=date_debut)
        if date_fin:
            mes_taches = mes_taches.filter(date_creation__lte=date_fin)
        #mes_taches = mes_taches.filter(statut = est_terminer) 
        paginator = Paginator(mes_taches, 5) 
        page = paginator.get_page(page_number)

    form = FilterTacheForm()
    return render(request,"taches_v1/acceuil.html",{'taches':page, 'form': form})  



@csrf_protect
@login_required(login_url='/login')
def create_tache(request):
    context ={}
    form = CreateTacheForm(request.POST or None)
    print("form---",form)
    if form.is_valid():
        form.user_id = request.user.id
        form.save()
        return redirect("/acceuil") 
         
    context['form']= form
    return render(request, "taches_v1/create_tache.html", context) 


@login_required(login_url='/login')
@csrf_protect
def edit_tache(request, id):
    context ={}
    obj = get_object_or_404(Tache, id = id)
    form = UpdateTacheForm(request.POST or None, instance = obj)
    if form.is_valid():
        form.save()
        return redirect("/acceuil") 
 
    context["form"] = form
 
    return render(request, "taches_v1/edit_tache.html", context) 
 

@login_required(login_url='/login')
@csrf_protect
def destroy(request, id):  
    tache = Tache.objects.get(id=id)  
    tache.delete()  
    return redirect("/acceuil")
