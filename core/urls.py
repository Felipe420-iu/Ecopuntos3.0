from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('iniciosesion/', views.iniciosesion, name='iniciosesion'),
    path('registrate/', views.registrate, name='registrate'),
    path('iniciosesionperfil/', views.iniciosesionperfil, name='iniciosesionperfil'),
    path('categorias/', views.categorias, name='categorias'),
    path('perfil/', views.perfil, name='perfil'),
    path('canjes/', views.canjes, name='canjes'),
    path('historial/', views.historial, name='historial'),
]

