from rest_framework import serializers

from .models import (
    Category,
    Post,
    Comment,
    CommentOnTheComment,
    LikePost,
    DisLikePost
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


class ValidateTitleAndContent:

    def validate_title(self, value):
        if len(value)<=3:
            raise serializers.ValidationError('El titulo debe contener al menos 4 caracteres')
        return value
    
    def validate_content(self, value):
        if len(value)<=20:
            raise serializers.ValidationError('El contenido de tu post es muy corto')
        return value


class CreatePostSerializer(serializers.ModelSerializer, ValidateTitleAndContent):

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
        

class UpdatePostSerializer(serializers.ModelSerializer, ValidateTitleAndContent):

    class Meta:
        model = Post
        fields = [
            'id',
            'category',
            'title',
            'content',
            'published'
        ]


class CommentCreateDeleteSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Comment
        fields = [
            'content'
        ]


class CommentOnTheCommentCreateDeleteSerializer(serializers.ModelSerializer):

    class Meta:
        model = CommentOnTheComment
        fields = [
            'content'
        ]


class CommentOnTheCommentSerializer(serializers.ModelSerializer):

    user = serializers.StringRelatedField()

    class Meta:
        model = CommentOnTheComment
        fields = [
            'id',
            'created_date',
            'user',
            'content',
        ]


class CommentListSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    comments_on_the_comments = serializers.SerializerMethodField()

    def get_comments_on_the_comments(self, obj):
        comments_on_the_comments = CommentOnTheComment.objects.filter(comment=obj, state=True).order_by('-id')
        serializer = CommentOnTheCommentSerializer(comments_on_the_comments, many=True)
        return serializer.data
    
    class Meta:
        model = Comment
        fields = [
            'id',
            'created_date',
            'user',
            'content',
            'comments_on_the_comments'
        ]


class ListPostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    category = serializers.StringRelatedField()
    comments = serializers.SerializerMethodField()
    likes = serializers.SerializerMethodField()

    def get_likes(self, obj):
        number_likes = LikePost.objects.filter(post=obj).count()
        return number_likes

    def get_comments(self, obj):
        comments = Comment.objects.filter(post=obj, state=True).order_by('-id')
        serializer = CommentListSerializer(comments, many=True)
        return serializer.data

    class Meta:
        model = Post
        fields = [
            'id',
            'slug',
            'created_date',
            'author',
            'published',
            'category',
            'title',
            'content',
            'likes',
            'comments',
        ]
























