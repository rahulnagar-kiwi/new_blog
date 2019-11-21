from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Data , Tag_Post, Tag
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
import datetime
from django.utils import timezone
# Create your views here.


def start_view(request):
    return render(request, 'execution/start_view.html')


def Logout(request):
    logout(request)
    return render(request, 'execution/start_view.html')


def Add(request):
    data = request.POST
    user_obj = request.user
    tag_list = request.POST.getlist('check_val')
    if not user_obj:
        return HttpResponse("it is not here")
    res = Data(blog_text=data['blog_text'], blog_title=data['blog_title'], username=user_obj)
    res.save()
    for obj1 in tag_list:
        var = Tag.objects.get(id=obj1)
        res2 = Tag_Post.objects.create(tag_mod=var, user_tag=user_obj, data_mod=res)
        res2.save()
    return redirect('/dash/')


def Login(request):
    return render(request, 'execution/login.html')


def Signup(request):
    return render(request, 'execution/signup.html')


def input_value(request):
    if request.method == "POST":
        data = request.POST
        obj = User.objects.create(username=data['user_name'], email=data['email'])
        obj.set_password(data['password'])
        obj.save()
        login(request, obj)
        return redirect('/dash/')


def Check_login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user:
        login(request, user)
        return redirect('/dash/')

    else:
        return HttpResponse("User Does Not Exist")


def redirect_add(request):
    t_obj = Tag.objects.all()
    return render(request, 'execution/add.html', {"t_obj": t_obj})


def my_profile(request):
        user_ref = request.user
        data_queryset = Data.objects.filter(username=user_ref).order_by('-creation_date')

        t_obj = Tag_Post.objects.all()
        context = {
            'data_queryset': data_queryset,
            't_obj': t_obj
        }

        return render(request, 'execution/profile.html', context)


def delete(request, id):
    obj = Data.objects.get(id=id)
    obj.delete()
    return redirect('/dash/')


def dashboard(request):
    t_obj = Tag_Post.objects.all()
    data_queryset =Data.objects.exclude(pub_date=None).order_by('-creation_date')
    # data_queryset =Data.objects.all(pub_date__isnone=False).order_by('-creation_date')
    context = {
        'data_queryset': data_queryset,
        't_obj': t_obj
    }
    return render(request, 'execution/data_index.html', context)


def edit(request, id):
    data_queryset = Data.objects.get(id=id)
    return render(request, "execution/edit.html", {"data_queryset":data_queryset})


def update(request, id):
    data = request.POST
    obj = Data.objects.get(id=id)
    obj.blog_text = data["blog_text"]
    obj.blog_title = data["blog_title"]
    obj.save()
    return redirect('/dash/')


def publish(request, id):
    obj = Data.objects.get(id=id)
    obj.pub_date = timezone.now()
    obj.save()
    return redirect('/dash/')

