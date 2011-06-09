from django import forms
from django.contrib.auth.models import User

from apps.tests.models import Test

class TestForm(forms.ModelForm):
    
    def clean_author(self):
        author = self.cleaned_data.get('author')
        try:
            user = User.objects.filter(username=author)
            return author
        except User.DoesNotExist:
            raise forms.ValidationError('No such User!')
    
    class Meta:
        model = Test
        exclude = ['author']