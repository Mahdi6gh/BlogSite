from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib import auth
# Create your views here.
def home(request):
    return render(request, 'homePageApp/index.html')
def detailpage(request):
    return render(request, 'homePageApp/post-details.html')
def LogIn(request):
    if request.user.is_authenticated:
        return redirect("home")
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('pass')
        print(f"Username: {username}, Password: {password}")  # Debugging
        user=auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.info(request, "invalid credentials")
            return redirect('login')
    else:
        return render(request, 'homePageApp/LogIn/index.html')
def LogOut(request):
    if request.user.is_authenticated:
        auth.logout(request)
    return redirect('home')
def register(request):
    return render(request, 'homePageApp/LogIn/Register.html')