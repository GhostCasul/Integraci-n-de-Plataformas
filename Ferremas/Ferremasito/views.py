from django.shortcuts import render

def Home(request):
    context={}
    return render(request, 'Ferremasito/Home.html', context)

def InicioSesion(request):
    context={}
    return render(request, 'Ferremasito/InicioSesion.html', context)

def Registro(request):
    context={}
    return render(request, 'Ferremasito/Registro.html', context)

def Api(request):
    context={}
    return render(request, 'Ferremasito/Api.html', context)