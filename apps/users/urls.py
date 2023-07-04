from django.urls import path

from . import views


urlpatterns = [

   # users/
    path('register/', views.UserRegister.as_view(), name='user_register'),
    path('list-all/', views.UserListAll.as_view(), name='user_list_all'),
    path('update/<int:pk>/', views.UserUpdateAPIView.as_view(), name='user_update'),
]