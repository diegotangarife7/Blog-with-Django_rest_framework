from rest_framework import serializers

from .models import (
    Category,
    Post,
    Comment,
    CommentOnTheComment
)




class CategorySerializer(serializers.ModelSerializer):

    user = serializers.SlugRelatedField(slug_field='name', read_only=True)

    class Meta:
        model = Category
        fields = [
            'id',
            'created_date',
            'modified_date',
            'name',
            'user',
            'state'
        ]

        read_only_fields = ['user']

    def validate_name(self, value):
        if len(value)<=3:
            raise serializers.ValidationError('El nombre de la categoria debe tener al menos 4 caracteres')

        return value

        
class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = [
            'id',
            'created_date',
            'author',
            'category',
            'title',
            'content',
            'published',
            'slug'
        ]  


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = [
            'id',
            'user',
            'post',
            'content'
        ]


class CommentOnTheCommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = CommentOnTheComment
        fields = [
            'id',
            'user',
            'comment',
            'content'
        ]