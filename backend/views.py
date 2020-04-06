from django.shortcuts import render, redirect
from backend.forms import Register, EditProfileForm, ExtendUserForm
from correction_app.forms import PostForm
from backend.models import ExtendUser
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.db import transaction

# Create your views here.
@login_required
def index(request):
    return render(request, 'backend/index.html')

def add_student(request):
    if request.method == 'POST':
        register_form = Register(request.POST)
        extend_form = ExtendUserForm(request.POST, request.FILES)
        if register_form.is_valid() and extend_form.is_valid():
            form1 = register_form.save()
            form2 = extend_form.save(commit=False)
            form2.user = form1
            extend_form.save()
            messages.success(request, 'Student have been registered successfully')
    else:
        register_form = Register()
        extend_form = ExtendUserForm(request.POST, request.FILES)
    return render(request, 'backend/add-student.html', {'reg':register_form, 'ext':extend_form})

@login_required
def my_profile(request):
    return render(request, 'backend/my-profile.html', {'view':request.user})

# @login_required
# def edit_form(request):
#     if request.method == 'POST':
#         edit_form = EditProfileForm(request.POST, instance=request.user)
#         if edit_form.is_valid():
#             edit_form.save()
#             return redirect('backend:my_profile')
#     else:
#         edit_form = EditProfileForm(instance=request.user)
#     return render(request, 'backend/edit-my-profile.html', {'edit':edit_form})

@transaction.atomic 
def edit_form(request):
    if request.method == 'POST':
        edit_form = EditProfileForm(request.POST, instance=request.user)
        extend = ExtendUserForm(request.POST, request.FILES, instance=request.user.extenduser)

        if edit_form.is_valid() and extend.is_valid():
            edit_form.save()
            extend.save()
    else:
        edit_form = EditProfileForm(instance=request.user)
        extend = ExtendUserForm(instance=request.user.extenduser)
    return render(request, 'backend/edit-my-profile.html', {'edit':edit_form, 'ext':extend})


@login_required
def pass_form(request):
    if request.method == 'POST':
        my_pass_form = PasswordChangeForm(data=request.POST, user=request.user)
        if my_pass_form.is_valid():
            my_pass_form.save()
            update_session_auth_hash(request, my_pass_form.user)
            return redirect('backend:my_profile')
    else:
        my_pass_form = PasswordChangeForm(user=request.user)
    return render(request, 'backend/change-password.html', {'pass':my_pass_form})








            

    



