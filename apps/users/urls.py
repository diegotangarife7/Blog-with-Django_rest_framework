from django.urls import path

from . import views


urlpatterns = [

   # users/
    path('register/', views.UserRegister.as_view(), name='user_register'),
    path('list-all/', views.UserListAll.as_view(), name='user_list_all'),
    path('detail/<int:pk>/', views.UserDetailAPIView.as_view(), name='user_detail'),
    path('update/<int:pk>/', views.UserUpdateAPIView.as_view(), name='user_update'),
    path('delete/<int:pk>/', views.UserDeleteAPIView.as_view(), name='user_delete'),
    path('password/update/<int:pk>/', views.UserPasswordUpdateAPIView.as_view(), name='user_update_password')
]