from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from .forms import signUpForm, AddRecordForm
from .models import customerRecord
# Create your views here.

def home(request):
    custRecords = customerRecord.objects.all()
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
        return render(request, 'home.html', {'custRecords':custRecords})


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

def userRecords(request, pk):
    if request.user.is_authenticated:
        record = customerRecord.objects.get(id=pk)
        return render(request, 'customerRecord.html', {'record': record})
    else:
        messages.success(request, "You have to Login to View this Page")
        return redirect('home')   

def deleteRecord(request, pk):   
    if request.user.is_authenticated:
        record = customerRecord.objects.get(id=pk)
        record.delete()
        messages.success(request, "Record Deleted Successfully")
        return redirect('home')
    else:
        messages.success(request, "You have to Login to Perform this Action")
        return redirect('home')   
    
def addRecord(request):
    userForm = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if userForm.is_valid():
                userForm.save()
                messages.success(request, "Record Added Successfully")
                return redirect('home')
            
        return render(request, 'addRecord.html', {'userForm': userForm})
    else:
        messages.success(request, "You have to Login to Perform this Action")
        return redirect('home')   
    
def updateRecord(request, pk):
    if request.user.is_authenticated:
        record = customerRecord.objects.get(id=pk)
        print(record)
        userForm = AddRecordForm(request.POST or None, instance= record) #Instance is used to fill the form with Customer data we need to update
        if userForm.is_valid():
            userForm.save()
            messages.success(request, "Record Updated Successfully")
            return redirect('home')
        return render(request, 'updateRecord.html', {'userForm': userForm})
    else:
        messages.success(request, "You have to Login to Perform this Action")
        return redirect('home')