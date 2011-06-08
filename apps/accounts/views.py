from django.contrib.auth.models import User
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login as _login, logout as _logout

from apps.accounts.forms import LoginForm,RegisterForm

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username = cd.get('username'),password=cd.get('password'))
            if user:
                _login(request,user)
                next=request.REQUEST.get('next','/index/')
                return HttpResponseRedirect(next)
            else:
                return HttpResponseRedirect(reverse('login'))
    else:
        form = LoginForm()
    rc = RequestContext(request,{'form':form})
    return render_to_response('accounts/login.html',rc)
    
def logout(request):
    _logout(request)
    return HttpResponseRedirect(reverse('login'))
    
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            dic = {
                   'username':form.cleaned_data.get('username'),
                   'first_name':form.cleaned_data.get('first_name'),
                   'last_name':form.cleaned_data.get('last_name'),
                   'email':form.cleaned_data.get('email'),
                   'is_active':True
                   }
            
            user = User(**dic)
            user.set_password(form.cleaned_data.get('password'))
            user.save()
            return HttpResponseRedirect(reverse('login'))
    else:
        form = RegisterForm()
    rc = RequestContext(request,{'form':form,'title':'Registration Form'})
    
    return render_to_response('accounts/registration.html',rc)












