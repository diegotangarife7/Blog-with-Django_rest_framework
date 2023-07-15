from django.shortcuts import get_object_or_404

from rest_framework.generics import (
    ListCreateAPIView, 
    UpdateAPIView, 
    DestroyAPIView, 
    ListAPIView, 
    CreateAPIView,
    RetrieveAPIView
    )
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny
from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import PermissionDenied

from .models import Category, Post, Comment
from .serializers import (
    CategorySerializer, 
    CreatePostSerializer,
    ListPostSerializer,
    UpdatePostSerializer,
    CommentCreateDeleteSerializer,
    CommentOnTheCommentCreateDeleteSerializer
    )
from .pagination import SmallResultsSetPagination



# -- Categories --

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
        kword = self.request.query_params.get('kword', None)
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

        if instance.user != request.user:
            raise PermissionDenied('No tienes permisos para actualizar esta categoria')
        
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
    

# -- Posts ---

class PostCreateAPIView(CreateAPIView):
    serializer_class = CreatePostSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = request.user
            serializer.save(author=user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostListAPIView(ListAPIView):
    serializer_class = ListPostSerializer
    permission_classes = [AllowAny]
    pagination_class = SmallResultsSetPagination

    def get_queryset(self):
        return Post.objects.filter(published=True, state=True).order_by('-created_date')


class PostDetailAPIView(RetrieveAPIView):
    serializer_class = ListPostSerializer
    permission_classes = [AllowAny]

    def get_object(self):
        slug = self.kwargs['slug']
        return get_object_or_404(Post, slug=slug)
        

class PostUpdateAPIView(UpdateAPIView):
    serializer_class = UpdatePostSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get_object(self, pk=None):
        return get_object_or_404(self.serializer_class.Meta.model, pk=pk, state=True)
    
    def update(self, request, *args, **kwargs):
        instance = self.get_object(kwargs.get('pk'))

        if instance.author != request.user:
            return Response({'message': 'No tienes permiso para actualizar este post.'}, status=status.HTTP_403_FORBIDDEN)

        serializer = self.get_serializer(instance, data=request.data, partial=self.partial_update)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Actualizado correctamente', 'data':serializer.data}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostDeleteAPIView(DestroyAPIView):
    serializer_class = UpdatePostSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get_object(self, pk=None):
        return get_object_or_404(self.serializer_class.Meta.model, pk=pk, state=True)
    
    def destroy(self, request, pk=None, *args, **kwargs):
        instance = self.get_object(pk=pk)
        if request.user == instance.author:
            instance.state = False
            instance.published = False
            instance.save()
            return Response({'message': 'Post eliminado con exito'}, status=status.HTTP_204_NO_CONTENT)
        
        return Response({'message': 'No puedes eliminar esta post'}, status=status.HTTP_401_UNAUTHORIZED)
    

class PostSearchByKwordAuthor(ListAPIView):
    serializer_class = ListPostSerializer

    def get_queryset(self):
        kword = self.request.query_params.get('kword', None)
        author = self.request.query_params.get('author', None)

        if kword and author:
            return Post.objects.filter(title__icontains=kword, author__name__icontains=author, state=True, published=True)
        elif kword:
            return Post.objects.filter(title__icontains=kword, state=True, published=True)
        elif author:
            return Post.objects.filter(author__name__icontains=author, state=True, published=True)
    
    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True)
        if queryset.exists():
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response({'message: No se encontraron post relacionados con tu busqueda'}, status=status.HTTP_404_NOT_FOUND)


class SeeMyPost(ListAPIView):
    serializer_class = ListPostSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get_queryset(self):
        user = self.request.user
        published = self.request.query_params.get('published', None)
        un_published = self.request.query_params.get('un_published', None)

        if published:
            return Post.objects.filter(state=True, author=user, published=True)
        elif un_published:
            return Post.objects.filter(state=True, author=user, published=False)
        else:
            return Post.objects.filter(state=True, author=user)
    
    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True)
        if queryset.exists():
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response({'message': 'No tienes ningun post'}, status=status.HTTP_204_NO_CONTENT)
    

# -- Comments ---

class CommentCreateAPIView(CreateAPIView):
    serializer_class = CommentCreateDeleteSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get_object(self):
        post_id = self.kwargs['pk']
        post = get_object_or_404(Post, pk=post_id)
        return post

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = request.user
            post = self.get_object()
            serializer.save(user=user, post=post)   
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class CommentDeleteAPIView(DestroyAPIView):
    serializer_class = CommentCreateDeleteSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get_object(self):
        pk = self.kwargs['pk']
        return get_object_or_404(self.serializer_class.Meta.model, pk=pk, state=True)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if request.user == instance.user:
            instance.state = False
            instance.save()
            return Response({'message': 'comentario eliminado'}, status=status.HTTP_204_NO_CONTENT)

        return Response({'message': 'Not Found'},status=status.HTTP_404_NOT_FOUND)
    

# -- Comments on the Comments ---

class CommentOnTheCommentCreateAPIView(CreateAPIView):
    serializer_class = CommentOnTheCommentCreateDeleteSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get_object(self):
        comment_id = self.kwargs['pk']
        print(comment_id)
        return get_object_or_404(Comment, pk=comment_id)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = request.user
            comment = self.get_object()
            serializer.save(user=user, comment=comment)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CommentOnTheCommentDeleteAPIView(DestroyAPIView):
    serializer_class = CommentOnTheCommentCreateDeleteSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get_object(self):
        pk = self.kwargs['pk']
        return get_object_or_404(self.serializer_class.Meta.model, pk=pk, state=True)
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if request.user == instance.user:
            instance.state = False
            instance.save()
            return Response({'message': 'comentario eliminado'}, status=status.HTTP_204_NO_CONTENT)
        
        return Response({'message': 'Not Found'},status=status.HTTP_404_NOT_FOUND)
    