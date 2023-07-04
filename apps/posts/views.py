from django.shortcuts import get_object_or_404

from rest_framework.generics import ListCreateAPIView, UpdateAPIView, DestroyAPIView, ListAPIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from rest_framework.authentication import TokenAuthentication

from .models import Category
from .serializers import CategorySerializer




class CategoryListCreateAPIView(ListCreateAPIView):
    serializer_class = CategorySerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        return Category.objects.all()
    
    def get_object(self, pk):
        return Category.objects.filter(pk=pk)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = request.user
            serializer.save(user=user)
            return Response({'Message': 'Categoria creada correctamente', 'data': serializer.data}, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def get(self, request, pk=None):
        if pk:
            serializer = self.serializer_class(self.get_object(pk), many=True)  
        else:   
            serializer = self.serializer_class(self.get_queryset(), many=True)

        return Response(serializer.data)
    

class CategorySearchKword(ListAPIView):
    serializer_class = CategorySerializer

    def get_queryset(self):
        kword = self.kwargs['kword']
        return Category.objects.filter(name__icontains=kword, state=True)
 
    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True)
        if queryset.exists():
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response({'message: No se encontraron categorias relacionadas con tu busqueda'}, status=status.HTTP_400_BAD_REQUEST)


class CategoryUpdateAPIView(UpdateAPIView):
    serializer_class = CategorySerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]

    def get_object(self, pk=None):
        return get_object_or_404(Category, pk=pk)
    
    def update(self, request, *args, **kwargs):
        instance = self.get_object(kwargs.get('pk'))
        serializer = self.get_serializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Categoria actualizada correctamente!'}, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
class CategoryDeleteAPIView(DestroyAPIView):
    serializer_class = CategorySerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]

    def get_object(self, pk=None):
        return get_object_or_404(Category, pk=pk, state=True)

    def destroy(self, request, pk=None, *args, **kwargs):
        instance = self.get_object(pk=pk)
        instance.state = False
        instance.save()
        return Response({'message': 'Categoria eliminada con exito'}, status=status.HTTP_204_NO_CONTENT)
    