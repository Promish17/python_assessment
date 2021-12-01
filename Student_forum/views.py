from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context

from .models import ForumSignup
from .forms import UserRegisterForm

# Create your views here.

#################### index#######################################
def index(request):
	return render(request, 'Student_forum/index.html', {'title':'index'})

########### register here #####################################
def forum_signup(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        for i in form:
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            print("email ------ %s", email)
            password = form.cleaned_data.get('password1')
            print("password ------ %s", password)
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')

            p = ForumSignup(username=username, email=email, first_name=first_name, last_name=last_name, password=password)
            p.save()
			######################### mail system ####################################
            htmly = get_template('Student_forum/Email.html')
            d = { 'username': email }
            subject, from_email, to = 'welcome', 'your_email@gmail.com', email
            html_content = htmly.render(d)
            msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()
			##################################################################
            messages.success(request, f'Your account has been created ! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
        print("I am here now.......")
    return render(request, 'Student_forum/register.html', {'form': form, 'title':'reqister here'})

################ login forms###################################################
def forum_login(request):
    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']
        print("username login %s", username)
        print('pass login %s', password)
        user = authenticate(request, username = username, password = password)
        if user is not None:
            form = login(request, user)
            messages.success(request, f' wecome {username} !!')
            return redirect('index')
        else:
            messages.info(request, f'Account does not exist, Please register.')
    form = AuthenticationForm()
    return render(request, 'Student_forum/login.html', {'form':form, 'title':'log in'})

