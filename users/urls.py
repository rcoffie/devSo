from django.urls import path
from users import views

urlpatterns = [
    path('', views.profiles, name='profile'),
    path('profile/<str:pk>/', views.profile, name='profile')
]
