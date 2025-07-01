from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('post-detail/', views.detailpage, name='detailpage'),
    path('post-detail/<int:post_id>/', views.detailpage, name='detailpage_with_id'),
    path('login/', views.LogIn, name='login'),
    path('logout/',views.LogOut,name='logout'), 
    path('register/',views.register,name='register'),
    path('blogs/',views.blogs,name="blogs"),
    path('blogs/<slug:slug>/', views.blog, name='blog_with_id'),
    path('about/',views.about,name="about"),
    path('contact/',views.contact,name="contact"),
    path('profile/', views.profile, name='profile'),

]