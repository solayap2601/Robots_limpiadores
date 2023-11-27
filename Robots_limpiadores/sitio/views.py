from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import LoginForm, RobotForm, HabitaForm
from django.contrib import messages
from .models import Robot

def inicio(request):
    return render(request, 'inicio.html')


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
    if request.method == 'POST':
        r =  request.POST['id']
        if Robot.objects.filter(id=r):
            x = Robot.objects.filter(id = int(r))[0]
            x.bateria = 100
            x.save()
        return redirect('inicio')

    
    return render(request, 'estacioncarga.html')

def plataforma(request):
    context ={
        'robots': ''
    }
    if request.method == 'POST':
        r = request.POST['id_plat']
        if Robot.objects.filter(plataforma=r):
            x = Robot.objects.filter(plataforma=r)
            context['robots'] = x.values()
            return render(request, 'mismatarea.html', context)
    return render(request, 'mismatarea.html')