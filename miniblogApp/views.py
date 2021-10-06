from django.shortcuts import render,HttpResponseRedirect
from django.contrib import messages
from .models import Post #importing the Post Model
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .forms import SignUpForm,LoginForm,PostForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib.auth.models import Group
# Create your views here.

#homepage_view function
def homepage_view(request):
    posts=Post.objects.all()
    return render(request, "miniblogApp/home.html",{"posts":posts})

#aboutpage_view function
def aboutpage_view(request):
    return render(request, "miniblogApp/about.html")

#contactpage_view function
def contactpage_view(request):
    # messages.success(request,"Thanks for Contacting")
    return render(request, "miniblogApp/contact.html")

#dashboard_view function
def dashboard_view(request):
    if request.user.is_authenticated:
        posts=Post.objects.all()
        return render (request, "miniblogApp/dashboard.html",{"posts":posts,"name":request.user.get_full_name()})
    else:
        return HttpResponseRedirect("/login/")

#signuppost_view function
def signuppost_view(request):
    if request.user.is_anonymous:
        if request.method=="POST":
            form=SignUpForm(request.POST)
            if form.is_valid():
                user=form.save()
                gp=Group.objects.get(name="Author")
                user.groups.add(gp)
                messages.success(request,"SignUp Successful")
        else:
            form=SignUpForm()
        return render(request,"miniblogApp/signup.html",{"form":form})
    else:
        return HttpResponseRedirect("/dashboard/")


#loginpost_view function
def loginpost_view(request):
    if request.user.is_anonymous:
        if request.method=="POST":
            form=LoginForm(request=request,data=request.POST)
            if form.is_valid():
                uname=form.cleaned_data["username"]
                password=form.cleaned_data["password"]
                user=authenticate(username=uname, password=password)
                if user is not None:
                    login(request, user)
                    return HttpResponseRedirect("/dashboard/")
        else:
            form=LoginForm()
        return render(request, "miniblogApp/login.html", {"form":form})
    else:
        return HttpResponseRedirect("/dashboard/")

#logoutpost_view function
def logoutpost_view(request):
    if request.user.is_authenticated:
        logout(request)
        return HttpResponseRedirect("/")
    else:
        return HttpResponseRedirect("/login/")

#addpost_view function
def addpost_view(request):
    if request.method=="POST":
        form=PostForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request," Post Added Successfully ! please click on cancel to go back to DashBoard")
            form=PostForm()
    else:
        form=PostForm()
    return render(request, "miniblogApp/addpost.html", {"form":form})

#updatepost_view function
def updatepost_view(request,id):
    if request.method == "POST":
        ps=Post.objects.get(pk=id)
        form=PostForm(request.POST,instance=ps)
        if form.is_valid():
            form.save()
            messages.success(request," Post Updated Successfully! please click on cancel to go back to DashBoard")
    else:
        ps=Post.objects.get(pk=id)
        form=PostForm(instance=ps)
    return render(request, "miniblogApp/updatepost.html", {"form":form})

#deletepost_view function
def deletepost_view(request,id):
    ps=Post.objects.get(pk=id)
    ps.delete()
    return HttpResponseRedirect("/dashboard/")
