from django.db import models
from datetime import date
from conf.validators import CustomValidators
from equipo.enum import EquipoPais, EquipoTrofeoOpcion, JugadorPie, \
    JugadorPosicion

# Create your models here.


class Equipo(models.Model):
    nombre = models.CharField(max_length=64, unique=True)
    escudo = models.ImageField(upload_to='escudos/', blank=True, null=True)
    pais = models.IntegerField(choices=EquipoPais.choices, default=EquipoPais.URUGUAY)
    fecha_fundado = models.DateField(null=True, blank=True)
    historia = models.TextField(null=True, blank=True)
    
    CREAR_TITULO_TEMPLATE = 'Crear equipo'
    EDITAR_TITULO_TEMPLATE = 'Editar datos del equipo' 
    
    def es_uruguay(self):
        return self.pais == EquipoPais.URUGUAY
           
    def get_jugadores(self):
        return Jugador.objects.filter(equipo=self)
    
    def get_trofeos(self):
        return EquipoTrofeo.objects.filter(equipo=self)
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        ordering = ["nombre"]
        verbose_name_plural = "Equipos"

        
class EquipoTrofeo(models.Model):
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    trofeo = models.IntegerField(choices=EquipoTrofeoOpcion.choices)
    cantidad = models.IntegerField(default=0)
    
    CREAR_TITULO_TEMPLATE = 'Vincular trofeo para el equipo' 
    EDITAR_TITULO_TEMPLATE = 'Editar trofeo para el equipo' 
    
    def __str__(self):
        return self.get_trofeo_display()
    
    class Meta:
        ordering = ["trofeo"]
        verbose_name_plural = "trofeo"
        unique_together = ["equipo", "trofeo"]


class Jugador(models.Model):
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    nombre_completo = models.CharField(max_length=64)
    fecha_nacimiento = models.DateField()
    altura = models.FloatField(null=True, blank=True, validators=[CustomValidators.valor_no_negativo])
    pie = models.IntegerField(choices=JugadorPie.choices, null=True, blank=True)
    fichado = models.DateField(null=True, blank=True)
    fin_contrato = models.DateField(null=True, blank=True)
    posicion = models.IntegerField(choices=JugadorPosicion.choices, default=JugadorPosicion.SIN_DEFINIR)
    salario = models.FloatField(default=0, validators=[CustomValidators.valor_no_negativo])
    valor_mercado = models.FloatField(default=0, validators=[CustomValidators.valor_no_negativo])
    
    CREAR_TITULO_TEMPLATE = 'Crear nuevo jugador para el equipo' 
    EDITAR_TITULO_TEMPLATE = 'Edición de los datos del jugador' 
    
    def activo(self):
        return self.fin_contrato > date.today()
    
    def get_fin_contrato(self):
        return self.fin_contrato
    
    def __str__(self):
        return '{0}'.format(self.nombre_completo)
    
    class Meta:
        ordering = ["nombre_completo"]
        verbose_name_plural = "Jugadores"
        permissions = (
            ("ver_salario", "Permite a los dirigentes ver el salario"),
        )

