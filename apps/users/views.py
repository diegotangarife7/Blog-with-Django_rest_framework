from django.shortcuts import get_object_or_404

from rest_framework.views import APIView, status
from rest_framework.generics import ListAPIView, UpdateAPIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.authtoken.models import Token

from .serializers import UserRegisterSerializer, UserListSerializer, UserUpdateSerializer


class UserRegister(APIView):

    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token, _ = Token.objects.get_or_create(user=user)
            return Response({
                'message': 'Usuario creado correctamente',
                'data': serializer.data,
                'token': token.key
            }, 
            status= status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class UserListAll(ListAPIView):
    permission_classes = [IsAdminUser]
    authentication_classes = [TokenAuthentication]
    serializer_class = UserListSerializer

    def get_queryset(self):
        return UserListSerializer.Meta.model.objects.all()

        
class UserUpdateAPIView(UpdateAPIView):
    serializer_class = UserUpdateSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_object(self, pk=None):
        return get_object_or_404(self.serializer_class.Meta.model, pk=pk)

    def update(self, request, *args, **kwargs):
        instance = self.get_object(kwargs.get('pk'))
        serializer = self.get_serializer(instance, data=request.data, partial=self.partial_update)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Usuario actualizado con exito'}, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)