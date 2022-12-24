from django.urls import path
from projects import views

urlpatterns = [
    path('', views.projects, name="projects"),
    path('project-detail/<str:pk>/', views.project_detail, name='project_detail'),
    path('create-project/', views.create_project, name="create_project")
]
