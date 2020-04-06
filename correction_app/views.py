from django.shortcuts import render
from django.contrib.auth.models import User
from correction_app.models import Post, Category, About, Service
from django.http import Http404
from correction_app.forms import BasicForm, StyleForm, MoreOptions, ValidateForm, PostForm
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

def index(request):
    home_srv = Service.objects.all()
    home_abt = About.objects.all()
    args = {'srv_key':home_srv, 'abt_key':home_abt}
    return render(request, 'correction_app/index.html', args)

def about(request):
    abt_data = About.objects.all()
    return render(request, 'correction_app/about.html', {'abt':abt_data})

def about_detail(request, abt_id):
    try:
        abt_detail = About.objects.get(id=abt_id)
    except About.DoesNotExist:
        Http404('The page you are accessing does not exist')
    return render(request, 'correction_app/about-detail.html', {'det_key':abt_detail})
        

def users(request):
    db_user = User.objects.all().order_by('-last_name')[:3]
    return render(request, 'correction_app/users.html', {'user_key':db_user})

def services(request):
    cat = Category.objects.all()
    return render(request, 'correction_app/services.html', {'cat':cat})

def list_cat(context):
    my_list = Category.objects.all()
    return {'cat_menu':my_list}


def contact(request):
    cat = Category.objects.all()
    return render(request, 'correction_app/contact.html', {'cat':cat})

def post_list(request, post_id):
    post_list = Post.objects.filter(cat__pk=post_id)
    my_list = Category.objects.all()
    return render(request, 'correction_app/post-list.html', 
    {'post_key':post_list, 'menu':my_list})

def post_detail(request):
    return render(request, 'correction_app/post-detail.html')


def more_form(request):
    form1 = MoreOptions()
    if request.method == 'POST':
        form2 = ValidateForm(request.POST)
        if form2.is_valid():
            print('Name'+form2.cleaned_data['name'], 'Subject'+form2.cleaned_data['subject'], 'Website'+form2.cleaned_data['website'])
            messages.success(request, 'Data printed to the console successfully')
    else:
        form2 = ValidateForm()
    args = {'form1':form1, 'form2':form2}
    return render(request, 'correction_app/more-forms.html', args)


def basic_form(request):
    if request.method == 'POST':
        basic_form = BasicForm(request.POST)
        if basic_form.is_valid():
            name = basic_form.cleaned_data['name']
            email = basic_form.cleaned_data['email']
            website = basic_form.cleaned_data['website']
            message = basic_form.cleaned_data['message']
            from_email = settings.EMAIL_HOST_USER 
            body = 'Name: {} Email: {} Website: {} Message: {}'.format(name, email, website, message)
            send_mail('Basic Email', body, from_email, ['uwazie.benedict@alabiansolutions.com'])
    else:
        basic_form = BasicForm()
        # style_form = StyleForm()
    args = {'key':basic_form}
    return render(request, 'correction_app/basic-form.html', args)

def post_form(request):
    if request.method == 'POST':
        pst_form = PostForm(request.POST, request.FILES)
        if pst_form.is_valid():
            pst_form.save(commit=True)
    else:
        pst_form = PostForm(request.POST, request.FILES)
    return render(request, 'correction_app/post-form.html', {'pst_key':pst_form})