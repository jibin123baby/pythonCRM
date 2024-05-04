from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from .forms import signUpForm

# Create your views here.

def home(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
         # Authenticate the user with the provided username and password
        user = authenticate(username=username, password=password)
       # print(username)
       # print(password)

        if user is None:
            # Display an error message if authentication fails (invalid password)
            messages.error(request, "Invalid User ID and Password")
            return redirect('home')
        else:
            # Log in the user and redirect to the home page upon successful login
            login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect('home')
    else:        
        return render(request, 'home.html', {})


def logoutUser(request):
    logout(request)
    messages.success(request, "Successfully Logged Out")
    return redirect('home')

def registertUser(request):
    if request.method == "POST":
        form = signUpForm(request.POST)
        if form.is_valid():
            form.save()
            #Authenticate and Login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)

            login(request, user)
            messages.success(request, "You have Successfully Registered")
            return redirect('home')
    else:
        form = signUpForm()
        return render(request, 'register.html', {'form': form})
        
    return render(request, 'register.html', {'form': form})
