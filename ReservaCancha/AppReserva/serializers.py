from rest_framework import serializers
from .models import Cancha, Disponibilidad, Reserva, Pago
from django.contrib.auth.models import User

class CanchaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cancha
        fields = '__all__'

class DisponibilidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disponibilidad
        fields = '__all__'

class ReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        fields = '__all__'

class PagoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pago
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'password']