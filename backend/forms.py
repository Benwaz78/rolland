from django import forms
from backend.models import ExtendUser
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.core import validators

class Register(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Username'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Enter Email'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}), label='Password')
    password2= forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}), label='Confirm Password')
    class meta():
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']

    def save(self, commit=True):
        user = super().save(commit=False)

        user.username = self.cleaned_data['username']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()
            return user

    
class ExtendUserForm(forms.ModelForm):

    
    class Meta():
        MALE = 'ML'
        FEMALE = 'FM'
        GENDER = [
            (MALE, 'Male'),
            (FEMALE, 'Female'),
        ]
        model = ExtendUser
        exclude = ('time', 'user')
        widgets = {
            'phone':forms.TextInput(attrs={'class':'form-control'}),
            'gender':forms.RadioSelect(choices=GENDER),
            'profile_pic':forms.ClearableFileInput()
        }


# EDIT YOUR PROFILE FORM

class EditProfileForm(UserChangeForm):

    class Meta():
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']