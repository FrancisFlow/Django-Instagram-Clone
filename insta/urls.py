from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('welcome', views.welcome, name='welcome'),
    path('profile/<profile_id>/', views.profile, name='profile'),
    path('post/<id>/', views.post_comment, name='comment'),
    path('new/profile/', views.new_profile, name='new-profile'),
]