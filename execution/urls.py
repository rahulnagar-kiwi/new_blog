from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.Login, name='login'),
    path('add/', views.Add, name='add'),
    path('signup/', views.Signup, name='signup'),
    path('front/', views.Front, name='front'),
    path('enter/', views.Enter, name='enter'),
    path('logout/', views.Logout, name='logout'),
    path('red/', views.redirect_add, name='redirect_add'),
    path('dash/', views.dashboard, name='dashboard'),
    path('blog/', views.Blogging, name='blogging'),
    path('check_login/', views.Check_login, name='check_login'),
    path('profile/', views.my_profile, name='my_profile'),
    path('edit/<id>/', views.edit, name='edit'),
    path('delete/<id>/', views.delete, name='delete'),
    path('update/<id>/', views.update, name='update'),
]