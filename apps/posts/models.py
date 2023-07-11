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
    like = models.PositiveIntegerField(default=0, verbose_name='Me gusta')
    dislike = models.PositiveIntegerField(default=0, verbose_name='No me gusta')
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


class Comment(BaseModel):
    # id
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, verbose_name='Usuario')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='Post', related_name='post')
    content = models.TextField(verbose_name='Contenido')
    like = models.PositiveIntegerField(default=0, verbose_name='Me gusta')
    
    def __str__(self):
        return self.content

    class Meta:
        db_table = 'Comment'
        verbose_name = 'Comentario'
        verbose_name_plural = 'Comentarios'
    

class CommentOnTheComment(BaseModel):
    # id
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, verbose_name='Usuario')
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, verbose_name='Comentario', related_name='comment')
    content = models.TextField(verbose_name='Contenido')
    like = models.PositiveIntegerField(default=0, verbose_name='Me gusta')

    def __str__(self):
        return self.content

    class Meta:
        db_table = 'CommentOnTheComment'
        verbose_name = 'Comentario del comentario'
        verbose_name_plural = 'Comentarios del comentario'

      