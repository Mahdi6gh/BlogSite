from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('post-detail/', views.detailpage, name='detailpage'),
    path('post-detail/<int:post_id>/', views.detailpage, name='detailpage_with_id'),
    path('login/', views.LogIn, name='login'),
    path('logout/',views.LogOut,name='logout'), 
    path('register/',views.register,name='register'),

]