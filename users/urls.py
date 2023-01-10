from django.urls import path
from users import views

urlpatterns = [
    path('', views.profiles, name='profiles'),
    path('profile/<str:pk>/', views.profile, name='profile'),
    path('user-login/', views.user_login, name='user_login'),
    path('user-registration/', views.user_registration, name="user_registration"),
    path('user-logout/',views.user_logout,name="user_logout")
]
