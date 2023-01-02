from django.shortcuts import render, redirect
from users.models import Profile, Skill
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm 

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


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # flash message needs to be here 
                return redirect('profile')
            else:
                print ("invalid username and password")
        else:
            print("invalid username and password")
    form = AuthenticationForm()
    return render(request, 'users/login.html',{'login_form':form})