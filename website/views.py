from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages

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