from django.db import models

# Create your models here.
class Cancha(models.Model):
    """Modelo de Cancha"""
    fecha = models.DateField()
    hora = models.TimeField()
    numero_cancha = models.IntegerField(primary_key=True, unique=True,null=False)
    precio = models.FloatField()
    def __str__(self):
        return f"{self.fecha} {self.hora} {self.numero_cancha} {self.precio}"

class Disponibilidad(models.Model):
    """Modelo de Disponibilidad de Cancha"""
    fecha = models.ForeignKey(Cancha, on_delete=models.CASCADE,related_name='disponibilidades_por_fecha')
    hora = models.ForeignKey(Cancha, on_delete=models.CASCADE, related_name='disponibilidades_por_hora')
    numero_cancha = models.ForeignKey(Cancha, on_delete=models.CASCADE, related_name='disponibilidades_por_cancha')
    disponible = models.BooleanField()
    def __str__(self):
        return f"{self.fecha} {self.hora} {self.numero_cancha} {self.disponible}"
    
class Reserva(models.Model):
   """Modelo de Reserva de Cancha"""
   user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
   numero_cancha = models.ForeignKey(Cancha, on_delete=models.CASCADE, related_name='reserva_cancha')
   fecha = models.ForeignKey(Cancha, on_delete=models.CASCADE, related_name='reserva_fecha')
   hora = models.ForeignKey(Cancha, on_delete=models.CASCADE, related_name='reserva_hora')
   pago = models.BooleanField()

   def __str__(self):
       return f"{self.user} {self.numero_cancha} {self.fecha} {self.hora} {self.pago}"
   
class Pago(models.Model):
    """Modelo de Pago de Reserva de Cancha"""
    reserva = models.ForeignKey(Reserva, on_delete=models.CASCADE, related_name='pagos_reserva')
    monto = models.FloatField()
    fecha_pago = models.DateField()
    metodo_pago = models.TimeField()
    def __str__(self):
        return f"{self.reserva} {self.monto} {self.fecha_pago} {self.metodo_pago}"
    