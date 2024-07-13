from django.contrib.auth.models import AbstractUser, Group, Permission, PermissionsMixin
from django.db import models
from django.core.exceptions import ValidationError
from django.conf import settings

class User(AbstractUser, PermissionsMixin):
    """Modelo de Usuario"""
    groups = models.ManyToManyField(
        Group,
        related_name="custom_user_set",  # related_name único
        blank=True,
        help_text=("The groups this user belongs to."),
        verbose_name=("groups"),
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="custom_user_permissions_set",  # related_name único
        blank=True,
        help_text=("Specific permissions for this user."),
        verbose_name=("user permissions"),
    )

    def __str__(self):
        return f"{self.username}"

class Register(models.Model):
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    rut = models.CharField(max_length=12, unique=True)
    edad = models.IntegerField()
    carrera = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, unique=True)
    duoc = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    confirm_password = models.CharField(max_length=50)
    objects = models.Manager()

    def __str__(self):
        return f"{self.nombre} {self.apellidos} {self.rut} {self.edad} {self.carrera} {self.email} {self.duoc} {self.password} {self.confirm_password}"

class Cancha(models.Model):
    """Modelo de Cancha"""
    fecha = models.DateField()
    hora = models.TimeField()
    numero_cancha = models.IntegerField(primary_key=True, unique=True, null=False)
    precio = models.FloatField()
    objects = models.Manager()  # Add this line to add the 'objects' member

    def save(self, *args, **kwargs):
        if Cancha.objects.count() >= 6 and not Cancha.objects.filter(pk=self.pk).exists():
            raise ValidationError("No se pueden agregar más de 6 canchas")
        super(Cancha, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.fecha} {self.hora} {self.numero_cancha} {self.precio}"

class Disponibilidad(models.Model):
    """Modelo de Disponibilidad de Cancha"""
    fecha = models.ForeignKey(Cancha, on_delete=models.CASCADE, related_name='disponibilidades_por_fecha')
    hora = models.ForeignKey(Cancha, on_delete=models.CASCADE, related_name='disponibilidades_por_hora')
    numero_cancha = models.ForeignKey(Cancha, on_delete=models.CASCADE, related_name='disponibilidades_por_cancha')
    disponible = models.BooleanField()
    objects = models.Manager()  # Add this line to add the 'objects' member

    def __str__(self):
        return f"{self.fecha} {self.hora} {self.numero_cancha} {self.disponible}"

class Reserva(models.Model):
    """Modelo de Reserva de Cancha"""
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    numero_cancha = models.ForeignKey(Cancha, on_delete=models.CASCADE, related_name='reserva_cancha')
    fecha = models.ForeignKey(Cancha, on_delete=models.CASCADE, related_name='reserva_fecha')
    hora = models.ForeignKey(Cancha, on_delete=models.CASCADE, related_name='reserva_hora')
    pago = models.BooleanField()
    objects = models.Manager()  # Add this line to add the 'objects' member

    def __str__(self):
        return f"{self.user} {self.numero_cancha} {self.fecha} {self.hora} {self.pago}"

class Pago(models.Model):
    """Modelo de Pago de Reserva de Cancha"""
    reserva = models.ForeignKey(Reserva, on_delete=models.CASCADE, related_name='pagos_reserva')
    monto = models.FloatField()
    fecha_pago = models.DateField()
    metodo_pago = models.TimeField()
    objects = models.Manager()  # Add this line to add the 'objects' member

    def __str__(self):
        return f"{self.reserva} {self.monto} {self.fecha_pago} {self.metodo_pago}"