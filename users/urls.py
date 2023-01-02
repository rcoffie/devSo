from django.urls import path
from users import views

urlpatterns = [
    path('', views.profiles, name='profile'),
    path('profile/<str:pk>/', views.profile, name='profile'),
    path('user-login/',views.user_login,name='user_login')
]
