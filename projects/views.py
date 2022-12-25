from django.shortcuts import render, HttpResponse, redirect
from projects.models import Project, Review, Tag
from projects.forms import ProjectForm
# Create your views here.


def projects(request):
    projects = Project.objects.all()
    context = {'projects': projects, }
    return render(request, 'projects/projects.html', context)


def project_detail(request, pk):
    project_detail = Project.objects.get(pk=pk)
    context = {'project_detail': project_detail}
    return render(request, 'projects/project_detail.html', context)


def create_project(request):
    form = ProjectForm()
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('projects')
    context = {'form': form}
    return render(request, 'projects/create_project.html', context)


def update_project(request, pk):
    project = Project.objects.get(pk=pk)
    form = ProjectForm(instance=project)
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            # return redirect('projects')
            return redirect('.')
    context = {'form': form}
    return render(request, 'projects/update_project.html', context)


def delete_project(request, pk):
    project = Project.objects.get(pk=pk)
    project.delete()
    return redirect('projects')
