from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from accounts.forms import UserLogin, UserRegistrationForm

# Create your views here.

def index(request):
    """ Return the index html file """
    return render(request, "index.html")
    
@login_required
def logout(request):
    """ log the user out """
    auth.logout(request)
    messages.success(request, "You have successfully been logged out!")
    return redirect(reverse('index'))
    
def login(request):
    """return a log in page"""
    if request.user.is_authenticated:
        return redirect(reverse('index'))
    if request.method == "POST":
        login_form = UserLogin(request.POST)
        
        if login_form.is_valid():
            user = auth.authenticate(username=request.POST['username'],
                                    password = request.POST['password'])
            if user:
                auth.login(user = user, request=request)
                messages.success(request, "you have successfully logged in!")
                return redirect(reverse('index'))
            else:
                login_form.add_error(None, "Your username or password is incorrect")
    else:
        login_form = UserLogin()
    return render(request, "login.html", {'login_form': login_form})
    
@login_required
def profile(request):
    """ a view that displayes a profile page of a logged in user """
    return render (request, "profile.html")
    
def registration(request):
    """ render the registration page"""
    if request.user.is_authenticated():
        return redirect(reverse('index'))
        
    if request.method=="POST":
        registration_form = UserRegistrationForm(request.POST)
        
        if registration_form.is_valid():
            registration_form.save()
            
            user = auth.authenticate(username = request.POST['username'],
                                        password = request.POST['password1'])
        
            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You have seccessfully registered.")
                return redirect(reverse('index'))
            else:
                messages.error(request, "Unable to register your account at this time.")
            
    registration_form = UserRegistrationForm()
    return render(request, "registration.html", { 'registration_form': registration_form })