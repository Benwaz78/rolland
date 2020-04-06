from django import forms
from django.core import validators
# This is my own module
from correction_app import my_validation_module
# It is ending
from correction_app.models import Post, Category
from django.contrib.auth.models import User


class BasicForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    website = forms.URLField(required=False)
    message = forms.CharField(widget=forms.Textarea)

class StyleForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter Name'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Enter Email'}))
    website = forms.URLField(required=False, widget=forms.URLInput(attrs={'class':'form-control'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}))

class MoreOptions(forms.Form):
    MALE = 'ML'
    FEMALE = 'FM'
    GENDER = [
        (MALE, 'Male'),
        (FEMALE, 'Female')
    ]

    FACEBOOK = 'FB'
    INSTAGRAM = 'IG'
    TWITTER = 'TW'
    NAIRALAND = 'NL'
    REFERER = [
        (FACEBOOK, 'Facebook'),
        (INSTAGRAM, 'Instagram'),
        (TWITTER, 'Twitter'),
        (NAIRALAND, 'Nairaland'),
    ]
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter Name'}))
    subject = forms.CharField(help_text="Make sure you supply 'Hello'", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter Sunject'}))
    email1 = forms.EmailField(label='Your Email', widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Enter Email'}))
    email2 = forms.EmailField(label='Confirm Email', widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Enter Email'}))
    website = forms.URLField(required=False, widget=forms.URLInput(attrs={'class':'form-control'}))
    gender = forms.CharField(widget=forms.RadioSelect(choices=GENDER))
    referer = forms.CharField(required=False, help_text='How did you hear about us', widget=forms.Select(choices=REFERER, attrs={'class':'form-control'}))
    message = forms.CharField(required=False, widget=forms.Textarea(attrs={'class':'form-control'}))


class ValidateForm(forms.Form):
    MALE = 'ML'
    FEMALE = 'FM'
    GENDER = [
        (MALE, 'Male'),
        (FEMALE, 'Female')
    ]

    FACEBOOK = 'FB'
    INSTAGRAM = 'IG'
    TWITTER = 'TW'
    NAIRALAND = 'NL'
    REFERER = [
        (FACEBOOK, 'Facebook'),
        (INSTAGRAM, 'Instagram'),
        (TWITTER, 'Twitter'),
        (NAIRALAND, 'Nairaland'),
    ]
    # The name field contains both custom validator and inbuilt
    name = forms.CharField(validators=[my_validation_module.start_with_c, validators.MaxLengthValidator(15)], widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter Name'}))
    subject = forms.CharField(help_text="Make sure you supply 'Hello'", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter Sunject'}))
    email1 = forms.EmailField(label='Your Email', widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Enter Email'}))
    email2 = forms.EmailField(label='Confirm Email', widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Enter Email'}))
    website = forms.URLField(required=False, widget=forms.URLInput(attrs={'class':'form-control'}))
    gender = forms.CharField(widget=forms.RadioSelect(choices=GENDER))
    referer = forms.CharField(required=False, help_text='How did you hear about us', widget=forms.Select(choices=REFERER, attrs={'class':'form-control'}))
    message = forms.CharField(required=False, widget=forms.Textarea(attrs={'class':'form-control'}))
    botcatcher = forms.CharField(required=False, widget=forms.HiddenInput, validators=[validators.MaxLengthValidator(1)])

    # VALIDATING FOR A SINGLE FIELD IN A FORM
    def clean_subject(self):
        subj = self.cleaned_data['subject']
        if 'Hello'.lower() not in subj:
            raise forms.ValidationError("You must include 'Hello' in the subject")
        return subj
      # END HERE
    
    # FIELD THAT DEPEND ON EACH OTHER
    def clean(self):
        my_clean = super().clean()
        em1 = my_clean.get('email1')
        em2 = my_clean.get('email2')

        if em1 != em2:
            raise forms.ValidationError('Your email and Confirm email do not match')
        elif not em1.endswith('@alabiansolutions.com'):
            raise forms.ValidationError("Email must end with '@alabiansolutions.com' ")
    # FIELD THAT END HERE


class PostForm(forms.ModelForm):

    poster = forms.ModelChoiceField(queryset=User.objects.all(), empty_label='Poster', widget=forms.Select(attrs={'class':'form-control'}))
    cat = forms.ModelMultipleChoiceField(queryset=Category.objects.all(), widget=forms.SelectMultiple(attrs={'class':'form-control'}))
    class Meta():
        model = Post
        exclude = ('created_date',)
        widgets = {
            'pst_title':forms.TextInput(attrs={'class':'form-control'}),
            'pst_img':forms.ClearableFileInput(),
            'content':forms.Textarea(attrs={'class':'form-control'}),
        }



    