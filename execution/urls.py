from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('login/', views.Login, name='login'),
    path('add/', views.Add, name='add'),
    path('signup/', views.Signup, name='signup'),
    path('start_view/', views.start_view, name='start_view'),
    path('input_value/', views.input_value, name='input_value'),
    path('logout/', views.Logout, name='logout'),
    path('redirect_add/', views.redirect_add, name='redirect_add'),
    path('dash/', views.dashboard, name='dashboard'),
    path('check_login/', views.Check_login, name='check_login'),
    path('profile/', views.my_profile, name='my_profile'),
    path('edit/<id>/', views.edit, name='edit'),
    path('delete/<id>/', views.delete, name='delete'),
    path('update/<id>/', views.update, name='update'),
    path('publish/<id>/', views.publish, name='publish'),
]

