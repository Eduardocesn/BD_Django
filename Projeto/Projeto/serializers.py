from rest_framework import serializers
from .models import Usuario
class ProjetoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id' ,'nome', 'cpf', 'data_nascimento']