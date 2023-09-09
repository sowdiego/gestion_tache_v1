from django.urls import path
from . import views


urlpatterns = [
   
    path('delete/<int:id>', views.destroy),  
    # URL de la page d'accueil
    path('acceuil/', views.acceuil, name='acceuil'),

    # URL pour créer une nouvelle tâche
    path('create_tache/', views.create_tache, name='create_tache'),

    # URL pour modifier une tâche existante (avec un paramètre d'ID)
    path('edit_tache/<int:id>/', views.edit_tache, name='edit_tache'),

    # URL pour l'inscription
    path('signup/', views.signup, name='signup'),

    # URL pour la connexion
    path('login/', views.user_login, name='login'),

    path('', views.user_login, name='login'),

    # URL pour la déconnexion
    path('logout/', views.logout_view, name='logout'),  # N'oubliez pas de définir cette vue dans views.py
]
