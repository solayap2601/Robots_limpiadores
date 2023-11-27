from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import LoginForm

def inicio(request):
    return render(request, 'inicio.html')

def login_plataforma(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.es_administrador:
                login(request, user)
                return redirect('nombre_de_tu_vista')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def login_robot(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and not user.es_administrador:
                login(request, user)
                return redirect('nombre_de_tu_vista')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})
