from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Data
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
import datetime
# Create your views here.


def start_view(request):
    return render(request, 'execution/start_view.html')


def Logout(request):
    logout(request)
    return render(request, 'execution/start_view.html')


def Add(request):
    data = request.POST
    user_obj = request.user
    if not user_obj:
        return HttpResponse("it is not here")
    res = Data(blog_text=data['blog_text'], blog_title=data['blog_title'], username=user_obj)
    res.save()
    data_queryset = Data.objects.filter(flag=True)
    return render(request, 'execution/data_index.html', {"data_queryset": data_queryset})


def Login(request):
    return render(request, 'execution/login.html')


def Signup(request):
    return render(request, 'execution/signup.html')


def input_value(request):
    if request.method == "POST":
        data = request.POST
#        res = User(user_name=data['user_name'], password=data['password'],email=data['email'])
        obj = User.objects.create(username=data['user_name'], email=data['email'])
        obj.set_password(data['password'])
        obj.save()

        login(request, obj)
#        obj = User.objects.get(username=data['user_name'])
        data_queryset = Data.objects.all()
        return render(request, 'execution/data_index.html', {'data_queryset': data_queryset})


def Check_login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user:
        data_queryset = Data.objects.all()
        login(request, user)
        return render(request, 'execution/data_index.html', {'data_queryset': data_queryset})
    else:
        return HttpResponse("User Does Not Exist")


def redirect_add(request):
    return render(request, 'execution/add.html')


def my_profile(request):
        user_ref = request.user
        data_queryset = Data.objects.filter(username=user_ref)
        context = {'data_queryset': data_queryset}
        return render(request, 'execution/profile.html', context)


def delete(request, id):
    obj = Data.objects.get(id=id)
    obj.delete()
    data_queryset = Data.objects.filter(flag=True)
    return render(request, 'execution/data_index.html', {"data_queryset": data_queryset})


def dashboard(request):
    data_queryset = Data.objects.filter(flag=True)
    return render(request, 'execution/data_index.html', {"data_queryset": data_queryset})


def edit(request, id):
    data_queryset = Data.objects.get(id=id)
    return render(request, "execution/edit.html", {"data_queryset":data_queryset})


def update(request, id):
    data = request.POST
    obj = Data.objects.get(id=id)
    obj.blog_text = data["blog_text"]
    obj.blog_title = data["blog_title"]
    obj.save()
    data_queryset = Data.objects.filter(flag=True)
    return render(request, 'execution/data_index.html', {"data_queryset": data_queryset})


def publish(request, id):
    obj = Data.objects.get(id=id)
    obj.flag = True
    obj.pub_date = datetime.datetime.now()
    obj.save()
    data_queryset = Data.objects.filter(flag=True)
    return render(request, 'execution/data_index.html', {"data_queryset": data_queryset})
