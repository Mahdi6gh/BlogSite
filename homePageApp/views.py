from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib import auth
from django.contrib.auth.models import User
from .models import blog as blogg
# Create your views here.
def home(request):
    blogs=blogg.objects.all()
    blogsCount=blogs.count()
    context={'blogs':blogs, 'blogsCount': blogsCount}
    return render(request, 'homePageApp/index.html',context)
def detailpage(request):
    return render(request, 'homePageApp/post-details.html')
def LogIn(request):
    if request.user.is_authenticated:
        return redirect("home")
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('pass')
        userr=auth.authenticate(request, username=username, password=password)
        if userr is not None:
            auth.login(request, userr)
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
    contex={'erors':[]}
    if request.user.is_authenticated:
        return redirect("home")
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('pass')
        password2 = request.POST.get('pass2')
        email=request.POST.get('email')
        lastname=request.POST.get('Lastname')
        firstname=request.POST.get('firstname')
        if password != password2:
            contex['erors'].append('Password match')
        if User.objects.filter(username=username).exists():
            contex['erors'].append('Username')
        if User.objects.filter(email=email).exists():
            contex['erors'].append('email')
        if len(contex['erors'])==0:
            userr=User.objects.create_user(username=username,password=password,email=email,first_name=firstname,last_name=lastname)
            auth.login(request,userr)
            return redirect('home')
        else:
            return render(request, 'homePageApp/LogIn/Register.html',contex)
        
    return render(request, 'homePageApp/LogIn/Register.html')
def blogs(request):
    blogs=blogg.objects.all()
    context={'blogs':blogs}
    return render(request,"homePageApp/blog.html",context)
def blog(request,id):
    YourBlog=blogg.objects.get(id=id)
    context={'blog':YourBlog}
    YourBlog.views+=1
    YourBlog.save()
    return render(request,"homePageApp/post-details.html",context)
def about(request):
    return render(request,"homePageApp/about.html")
def contact(request):   
    return render(request,"homePageApp/contact.html")
def profile(request):
    if not request.user.is_authenticated:
        return redirect("login")
    try:
        profile = request.user.profile
    except:
        user=request.user
    user=request.user
    return render(request, "homePageApp/profile.html", {'user': user,'profile': profile })