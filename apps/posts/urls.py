from django.urls import path

from . import views


          # posts/
urlpatterns = [

          # category 
     path('categories/', views.CategoryListCreateAPIView.as_view()),
     path('categories/<int:pk>/', views.CategoryListCreateAPIView.as_view()),
     path('category/update/<int:pk>/', views.CategoryUpdateAPIView.as_view()),
     path('category/delete/<int:pk>/', views.CategoryDeleteAPIView.as_view()),
     path('categories/search/', views.CategorySearchKword.as_view()),

          # posts
     path('create/', views.PostCreateAPIView.as_view()),
     path('list/all/', views.PostListAPIView.as_view()),
     path('detail/<slug>/', views.PostDetailAPIView.as_view()),
     path('update/<int:pk>/', views.PostUpdateAPIView.as_view()),
     path('delete/<int:pk>/', views.PostDeleteAPIView.as_view()),
     path('search/', views.PostSearchByKwordAuthor.as_view()),
     path('see/all/', views.SeeMyPost.as_view()),

          # Comments
     path('comment/create/<int:pk>/', views.CommentCreateAPIView.as_view()),
     path('comment/delete/<int:pk>/', views.CommentDeleteAPIView.as_view()),

          # Comments on the Comments
     path('comment/on/the/comment/create/<int:pk>/', views.CommentOnTheCommentCreateAPIView.as_view()),
     path('comment/on/the/comment/delete/<int:pk>/', views.CommentOnTheCommentDeleteAPIView.as_view()),

          # like and dis like
     path('like/<int:pk>/', views.PostLike.as_view()),
     path('like/delete/<int:pk>/', views.PostLike.as_view()),
     path('dislike/<int:pk>/', views.PostDisLike.as_view()),
     path('dislike/delete/<int:pk>/', views.PostDisLike.as_view()),


]
          