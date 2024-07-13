from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Register, Cancha, Disponibilidad, Reserva, Pago

# Registrar el modelo de Usuario Personalizado
admin.site.register(User, UserAdmin)

# Registrar otros modelos
admin.site.register(Register)
admin.site.register(Cancha)
admin.site.register(Disponibilidad)
admin.site.register(Reserva)
admin.site.register(Pago)