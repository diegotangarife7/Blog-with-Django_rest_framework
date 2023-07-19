from django.contrib import admin

from .models import (
    Category,
    Post,
    LikePost,
    DisLikePost,
    Comment,
    CommentOnTheComment,
    Image
    )

    
admin.site.register(Image)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'user', 'state', 'created_date', 'modified_date', 'deleted_date']
    search_fields = ["name"]
    list_filter = ['state']
admin.site.register(Category, CategoryAdmin)


class LikePostAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'post', 'quantity']
admin.site.register(LikePost, LikePostAdmin)


class DisLikePostAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'post', 'quantity']
admin.site.register(DisLikePost, DisLikePostAdmin)


class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'category', 'title', 'content', 'published', 'state', 'created_date', 'modified_date', 'deleted_date']
    search_fields = ["title"]
    list_filter = ['state', 'published']
admin.site.register(Post, PostAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'post', 'content', 'state', 'created_date']
    list_filter = ['state']
admin.site.register(Comment, CommentAdmin)


class CommentOnTheCommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'comment', 'user', 'content', 'state', 'created_date']
    list_filter = ['state']
admin.site.register(CommentOnTheComment, CommentOnTheCommentAdmin)