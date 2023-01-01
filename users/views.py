from django.shortcuts import render
from users.models import Profile, Skill

# Create your views here.


def profiles(request):
    profiles = Profile.objects.all()
    context = {'profiles':profiles}
    return render(request, 'users/profiles.html',context)

def profile(request, pk):
    profile = Profile.objects.get(pk=pk)
    skills = Skill.objects.filter(owner=profile)
    context = {'profile':profile,'skills':skills}
    return render(request, 'users/profile.html/',context)