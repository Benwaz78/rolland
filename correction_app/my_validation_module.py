from django import forms
from django.core import validators

def start_with_c(value):
    if value[0].lower() != 'c':
        raise forms.ValidationError('Name must start with c')
    