from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

class Usuario(AbstractUser):
    es_administrador = models.BooleanField(default=False)

    # Agrega estos campos para solucionar los errores
    groups = models.ManyToManyField(
        Group,
        verbose_name='groups',
        blank=True,
        help_text=(
            'The groups this user belongs to. A user will get all permissions '
            'granted to each of their groups.'
        ),
        related_name="usuario_set",  # Aquí está el cambio
        related_query_name="user",
    )

    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name="usuario_set",  # Aquí está el cambio
        related_query_name="user",
    )

class Plataforma(models.Model):
    pass  # No necesitamos definir los campos de robots y habitaciones aquí

class Robot(models.Model):
    ESTADOS = (
        ('1', 'Disponible'),
        ('2', 'Ocupado'),
    )
    id = models.AutoField(primary_key=True)
    estado = models.CharField(max_length=1, choices=ESTADOS)
    ubicacion = models.ForeignKey('Habitacion', on_delete=models.SET_NULL, null=True)
    bateria = models.IntegerField()
    mapa = models.TextField()  # Esto podría ser un campo JSON, dependiendo de cómo quieras manejarlo
    plataforma = models.ForeignKey('Plataforma', on_delete=models.CASCADE)  # Aquí definimos la relación con Plataforma

class EstacionDeCarga(models.Model):
    ubicacion = models.CharField(max_length=255)
    capacidad = models.IntegerField()
    robots = models.ManyToManyField('Robot')

class Habitacion(models.Model):
    ESTADOS = (
        ('1', 'Limpio'),
        ('2', 'Sucio'),
    )
    TIPOS = (
        ('1', 'Individual'),
        ('2', 'Doble'),
        # Agrega más tipos según sea necesario
    )
    numero = models.CharField(max_length=10)
    estado = models.CharField(max_length=1, choices=ESTADOS)
    tipo = models.CharField(max_length=1, choices=TIPOS)
    plataforma = models.ForeignKey('Plataforma', on_delete=models.CASCADE)  # Aquí definimos la relación con Plataforma
