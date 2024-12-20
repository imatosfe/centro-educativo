# estudiantes/models.py
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone


from seccion.models import Secciones


class Estudiante(models.Model):
    Ciudades = [
  
    ('A', 'Azua'),
    ('BH', 'Bahoruco'),
    ('BA', 'Barahona'),
    ('D', 'Dajabón'),
    ('DN', 'Distrito Nacional'),
    ('DU', 'Duarte'),
    ('EP', 'Elías Piña'),
    ('ES', 'El Seibo'),
    ('E', 'Espaillat'),
    ('H', 'Hato Mayor'),
    ('HM', 'Hermanas Mirabal'),
    ('I', 'Independencia'),
    ('LA', 'La Altagracia'),
    ('LR', 'La Romana'),
    ('LV', 'La Vega'),
    ('MTS', 'María Trinidad Sánchez'),
    ('MN', 'Monseñor Nouel'),
    ('MC', 'Monte Cristi'),
    ('MT', 'Monte Plata'),
    ('P', 'Pedernales'),
    ('PR', 'Peravia'),
    ('PP', 'Puerto Plata'),
    ('S', 'Samaná'),
    ('SR', 'Sánchez Ramírez'),
    ('SC', 'San Cristóbal'),
    ('SJO', 'San José de Ocoa'),
    ('SJ', 'San Juan'),
    ('SPM', 'San Pedro de Macorís'),
    ('SA', 'Santiago'),
    ('SAR', 'Santiago Rodríguez'),
    ('SD', 'Santo Domingo'),
    ('V', 'Valverde'),
  
]
    
    
    Tipo = [
    ('A','Activo'),
    ('I','Inactivo'),
  
  
]
    # Datos personales
    nombre = models.CharField(max_length=50, verbose_name= "Nombres")
    apellido = models.CharField(max_length=50, verbose_name="Aplleidos")
    fecha_nacimiento = models.DateField()
    genero = models.CharField(
        max_length=10,
        choices=[('M', 'Masculino'), ('F', 'Femenino'), ('O', 'Otro')],
        default='O'
    )
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=15, blank=True, null=True)

    # Dirección
    direccion = models.CharField(max_length=255)
    ciudad = models.CharField(choices=Ciudades, max_length=50)
    

    estado = models.CharField(choices=Tipo,max_length=50)
   

    # Información académica
    matricula = models.CharField(max_length=20, unique=True)
    fecha_ingreso = models.DateField(default=timezone.now)
  
    anio_escolar = models.CharField(max_length=10)  # Ej: 2024-2025

    seccion = models.ForeignKey(Secciones, on_delete=models.CASCADE, related_name='estudiantes', blank=True, null=True)
    tarifa_personalizada = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        validators=[MinValueValidator(0)],
        blank=True, 
        null=True
    )

    def obtener_precio_anual(self):
        return self.tarifa_personalizada or self.seccion.grado.tarifa_escolar.precio_anual

    def obtener_precio_mensual(self):
        return self.obtener_precio_anual() / 12
    
    
    # Métodos especiales
    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.matricula}"
    
    def obtener_calificaciones_por_grado(self, grado):
        return self.calificaciones.filter(grado=grado)
    


    def calcular_promedio_por_grado(self, grado):
        calificaciones = self.obtener_calificaciones_por_grado(grado)
        if not calificaciones.exists():
            return None
        return calificaciones.aggregate(promedio=models.Avg('nota'))['promedio']
  

    class Meta:
        ordering = ['apellido', 'nombre']
        verbose_name = "Estudiante"
        verbose_name_plural = "Estudiantes"

 