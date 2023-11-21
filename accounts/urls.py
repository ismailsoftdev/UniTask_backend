# accounts/urls.py

from django.urls import path
from accounts import views

urlpatterns = [
    path('users/profile/<int:pk>/', views.UserProfile.as_view()),
    path('users/create/', views.UserCreate.as_view()),
    path('users/update/<int:pk>/', views.UserUpdate.as_view()),
    path('users/deactivate/<int:pk>/', views.UserDeactivate.as_view()),
    
    path('login/', views.UserLogin.as_view()),
]
