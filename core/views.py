from django.shortcuts import render, HttpResponse

def index(request):
    return render(request, 'core/index.html')

def iniciosesion(request):
    return render(request, 'core/iniciosesion.html')

def registrate(request):
    return render(request, 'core/registrate.html')

def iniciosesionperfil(request):
    return render(request, 'core/iniciosesionperfil.html')

def categorias(request):
    return render(request, 'core/categorias.html')

def perfil(request):
    return render(request, 'core/perfil.html')

def canjes(request):
    return render(request, 'core/canjes.html')

def historial(request):
    return render(request, 'core/historial.html')