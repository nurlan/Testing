from django import forms
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(max_length=20,widget=forms.PasswordInput(attrs={'minlength':'6'}))
    
class RegisterForm(forms.Form):
    
    username = forms.CharField(max_length=20)
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)
    email = forms.EmailField()
    password = forms.CharField(max_length=20,widget=forms.PasswordInput(attrs={'minlength':'6'}))
    cpassword = forms.CharField(max_length=20,widget=forms.PasswordInput(attrs={'minlength':'6'}))
    
    def clean(self):
        password = self.cleaned_data.get('password')
        cpassword = self.cleaned_data.get('cpassword')
        
        if password != cpassword:
            raise forms.ValidationError('Password mismatch!')
        return self.cleaned_data
    
    def clean_username(self):
        username = self.cleaned_data.get('username')
        q = User.objects.filter(username=username)
        
        if q.count():
            raise forms.ValidationError('Username already exists!')
        return username