from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import LoginForm, RobotForm, HabitaForm
from django.contrib import messages
from .models import Robot

def inicio(request):
    return render(request, 'inicio.html')

def login_plataforma(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('inicio')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def robot_registration(request):
    if request.method == 'POST':
        form = RobotForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Robot creado con exito')
            return redirect('inicio')
    else:
        context = {}
        context['form'] = RobotForm()
    return render(request,'registration.html',context)

def Habita_registration(request):
    if request.method == 'POST':
        form = HabitaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Habitacion creado con exito')
            return redirect('inicio')
    else:
        context = {}
        context['form'] = HabitaForm()
    return render(request,'registration.html',context)

def mostrar_robot(request):
    context = { 
        'listarobots':Robot.objects.all().values()
    }
    return render(request, 'most_robot.html',context)

def mandar_estacion(request):
    return render(request, 'estacioncarga.html')