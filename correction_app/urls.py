from django.urls import path
from correction_app import views

app_name = 'correction_app'

urlpatterns = [
    path('', views.users, name='users'),
    path('services-page/', views.services, name='services'),
    path('post-detail/', views.post_detail, name='post_detail'),  
    path('contact-page/', views.contact, name='contact'),  
    path('basic-form/', views.basic_form, name='basic_form'),  
    path('more-form/', views.more_form, name='more_form'),  
    path('post-form/', views.post_form, name='post_form'),  
]