from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Create your views here.
def LoginView(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('landingpage')
    else:
        return render(request,'index.html')


def SignupView(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Account Created Successfully!')
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('landing-page')   
    else:
        return render(request,'signup.html')
    
def LogoutView(request):
    logout(request)
    messages.success(request,'Logout Successful!')
    return redirect('login')

def LandingView(request):
    return render(request,'landingpage.html')