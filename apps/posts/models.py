import random

from django.db import models
from django.conf import settings
from django.utils.text import slugify

from apps.base.models import BaseModel 


class Category(BaseModel):
    # id
    name = models.CharField(max_length=200, verbose_name='Categoria', unique=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, verbose_name='usuario')

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'Category'
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'


class Post(BaseModel):
    # id
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, verbose_name='Autor')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Categoria')
    title = models.CharField(max_length=120, verbose_name='Titulo')
    content = models.TextField(verbose_name='Contenido')
    published = models.BooleanField(default=True, verbose_name='Publicado')
    slug = models.CharField(max_length=300, verbose_name='Slug', blank=True, null=True)
    # image = 

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)

        if Post.objects.filter(slug=self.slug).exists():
            self.slug = f'{self.slug}-{random.randint(1000, 100000)}'

        super().save(*args, **kwargs)

    class Meta:
        db_table = 'Post'
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'


class LikePost(BaseModel):
    # id
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='usuario')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name="Post", related_name='likes')
    quantity = models.PositiveIntegerField(default=0, verbose_name='cantidad')

    def __str__(self):
        return str(self.quantity)
    
    class Meta:
        unique_together = ['user', 'post']
        db_table = 'like_post'
        verbose_name = 'like'
        verbose_name_plural = 'likes'


class DisLikePost(BaseModel):
    # id
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='usuario')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name="Post", related_name='dis_likes')
    quantity = models.PositiveIntegerField(default=0, verbose_name='cantidad')

    def __str__(self):
        return str(self.quantity)
    
    class Meta:
        unique_together = ['user', 'post']
        db_table = 'dis_like_post'
        verbose_name = 'dis_like'
        verbose_name_plural = 'dis_likes'




class Comment(BaseModel):
    # id
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, verbose_name='Usuario')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='Post', related_name='comments')
    content = models.TextField(verbose_name='Contenido')
    
    def __str__(self):
        return self.content

    class Meta:
        db_table = 'Comment'
        verbose_name = 'Comentario'
        verbose_name_plural = 'Comentarios'
    

class CommentOnTheComment(BaseModel):
    # id
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, verbose_name='Usuario')
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, verbose_name='Comentario', related_name='comments_on_the_comments')
    content = models.TextField(verbose_name='Contenido')

    def __str__(self):
        return self.content

    class Meta:
        db_table = 'CommentOnTheComment'
        verbose_name = 'Comentario del comentario'
        verbose_name_plural = 'Comentarios del comentario'

      