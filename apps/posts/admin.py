from django.contrib import admin

from .models import Category, Post, Comment, CommentOnTheComment


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'user', 'state', 'created_date', 'modified_date', 'deleted_date']
admin.site.register(Category, CategoryAdmin)


class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'category', 'title', 'content', 'published', 'like', 'dislike', 'state', 'created_date', 'modified_date', 'deleted_date']
admin.site.register(Post, PostAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'post', 'content', 'like', 'state', 'created_date']
admin.site.register(Comment, CommentAdmin)


class CommentOnTheCommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'comment', 'content', 'like', 'state', 'created_date']
admin.site.register(CommentOnTheComment, CommentOnTheCommentAdmin)