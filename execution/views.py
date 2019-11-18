from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Data
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
# Create your views here.


def Front(request):
    return render(request, 'execution/front.html')


def Logout(request):
    logout(request)
    return render(request,'execution/front.html')


def Add(request):
    d = request.POST
    p = request.user
    if not p:
        return HttpResponse("it is not here")
    res = Data(blog_text=d['blog_text'], blog_title=d['blog_title'], username=p)
    res.save()
    data_queryset = Data.objects.all()
    return render(request, 'execution/content.html', {'data_queryset': data_queryset})


def Login(request):
    return render(request, 'execution/login.html')


def Signup(request):
    return render(request, 'execution/signup.html')


def Enter(request):
    if request.method == "POST":
        data = request.POST
#        res = User(user_name=data['user_name'], password=data['password'],email=data['email'])
        obj = User.objects.create(username=data['user_name'], email=data['email'])
        obj.set_password(data['password'])
        obj.save()

        login(request, obj)
#        obj = User.objects.get(username=data['user_name'])
        data_queryset = Data.objects.all()
        return render(request, 'execution/content.html', {'data_queryset': data_queryset})


def Blogging(request):
    HttpResponse("you are at the blogging view")


def Check_login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user:
        data_queryset = Data.objects.all()
        login(request, user)
        return render(request, 'execution/content.html', {'data_queryset': data_queryset})
    else:
        return HttpResponse("User Does Not Exist")


def redirect_add(request):
    return render(request, 'execution/add.html')


def my_profile(request):
        u = request.user
        whole = Data.objects.filter(username=u)
        context = {'whole': whole}
        return render(request, 'execution/profile.html', context)


def delete(request, id):
    obj = Data.objects.get(id=id)
    obj.delete()
    data_queryset = Data.objects.all()
    context = {'data_queryset': data_queryset,
     }
    return render(request, 'execution/content.html', context)


def dashboard(request):
    data_queryset = Data.objects.all()
    context = {'data_queryset': data_queryset,
               }
    return render(request, 'execution/content.html', context)


def edit(request, id):
    data_queryset = Data.objects.get(id=id)
    return render(request, "execution/edit.html", {"data_queryset":data_queryset})


def update(request, id):
    h = request.POST
    obj = Data.objects.get(id=id)
    obj.blog_text = h["blog_text"]
    obj.blog_title = h["blog_title"]
    obj.save()
    data_queryset = Data.objects.all()
    return render(request, 'execution/content.html', {"data_queryset": data_queryset})
