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

          # post
     path('create/', views.PostCreateAPIView.as_view()),
     path('list/all/', views.PostListAPIView.as_view()),
     path('detail/<slug>/', views.PostDetailAPIView.as_view()),
     path('update/<int:pk>/', views.PostUpdateAPIView.as_view()),
     path('delete/<int:pk>/', views.PostDeleteAPIView.as_view()),
     path('search/', views.PostSearchByKwordAuthor.as_view()),

]
