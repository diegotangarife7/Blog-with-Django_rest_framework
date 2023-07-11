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


class CreatePostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = [
            'id',
            'author',
            'category',
            'title',
            'content',
        ]  

        extra_kwargs = {
                'author': {'read_only': True}, 
            }


class UpdatePostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = [
            'id',
            'category',
            'title',
            'content',
            'published'
        ]
        

class CommentOnTheCommentSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()

    class Meta:
        model = CommentOnTheComment
        fields = [
            'id',
            'user',
            'content'
        ]


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    comment_the_comment = CommentOnTheCommentSerializer(many=True, read_only=True, source='comment')

    class Meta:
        model = Comment
        fields = [
            'id',
            'user',
            'content',
            'comment_the_comment'
        ]


class ListPostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    category = serializers.StringRelatedField()
    comments = CommentSerializer(many=True, read_only=True, source='post')

    class Meta:
        model = Post
        fields = [
            'id',
            'slug',
            'created_date',
            'author',
            'category',
            'title',
            'content',
            'like',
            'dislike',
            'comments'
        ]
        
























