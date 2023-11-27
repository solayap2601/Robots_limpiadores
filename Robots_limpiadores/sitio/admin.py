from django.contrib import admin
from .models import Plataforma, Robot, EstacionDeCarga, Habitacion, Usuario

admin.site.register(Usuario)
admin.site.register(Plataforma)
admin.site.register(Robot)
admin.site.register(EstacionDeCarga)
admin.site.register(Habitacion)