from django.urls import path
from backend import views
from django.contrib.auth import views as auth_views

app_name = 'backend'

urlpatterns = [
    path('', views.index, name='index'),
    path('add-student/', views.add_student, name='add_student'),
    path('my-profile/', views.my_profile, name='my_profile'),
    path('edit-form/', views.edit_form, name='edit_form'),
    path('pass-form/', views.pass_form, name='pass_form'),
    path('login_page/', auth_views.LoginView.as_view(template_name='backend/login.html'), name='login'),
    path('logout-page/', auth_views.LogoutView.as_view(template_name='backend/logout.html'), name='logout'),
 

]