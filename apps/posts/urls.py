from django.urls import path

from . import views

urlpatterns = [

     # posts/
     path('categories/', views.CategoryListCreateAPIView.as_view()),
     path('categories/<int:pk>/', views.CategoryListCreateAPIView.as_view()),
     path('category/update/<int:pk>/', views.CategoryUpdateAPIView.as_view()),
     path('category/delete/<int:pk>/', views.CategoryDeleteAPIView.as_view()),
     path('categories/search/<str:kword>/', views.CategorySearchKword.as_view())
]
