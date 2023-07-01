from rest_framework.views import APIView, status
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAdminUser
from rest_framework.authtoken.models import Token

from .serializers import UserRegisterSerializer, UserListSerializer


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


        
