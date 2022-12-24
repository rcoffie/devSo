from django.shortcuts import render, HttpResponse
from projects.models import Project, Review, Tag
from projects.forms import ProjectForm
# Create your views here.


def projects(request):
    projects = Project.objects.all()
    context = {'projects': projects, }
    return render(request, 'projects/projects.html', context)


def project_detail(request, pk):
    project_detail = Project.objects.get(pk=pk)
    context = {'project_detail':project_detail}
    return render(request, 'projects/project_detail.html',context)

def create_project(request):
    form = ProjectForm()
    context = {'form':form}

    return render(request, 'projects/create_project.html',context)
