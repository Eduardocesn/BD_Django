from django.http import JsonResponse
from .models import Usuario
from .serializers import ProjetoSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET', 'POST'])
def usuarios_list(request, format=None):

    if request.method == 'GET':
        usuarios = Usuario.objects.all()
        serializer = ProjetoSerializer(usuarios, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = ProjetoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])        
def usuario_detalhe(request, id, format=None):
    try:
        usuario = Usuario.objects.get(pk=id)
    except Usuario.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = ProjetoSerializer(usuario)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = ProjetoSerializer(usuario, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        usuario.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)