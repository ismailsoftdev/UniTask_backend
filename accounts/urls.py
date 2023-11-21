# accounts/urls.py

from django.urls import path
from accounts import views

urlpatterns = [
    path('user/create/', views.UserRegistrationView.as_view(), name='user-create'),
    path('user/update/', views.UserUpdateView.as_view(), name='user-update'),
    path('user/deactivate/<int:pk>/',
         views.UserDeactivateView.as_view(), name='user-deactivate'),
    path('user/profile/', views.UserProfileView.as_view(), name='user-profile'),
    
    path('login/', views.UserLoginView.as_view(), name='user-login'),
    path('register/', views.UserRegistrationView.as_view(), name='user-register'),
]
