from django import forms

from .models import Join

class EmailForm(forms.Form):
    """docstring for EmailForm"""
    name = forms.CharField(required=False)
    email = forms.EmailField()

class JoinForm(forms.ModelForm):
    """docstring for JoinForm"""
    class Meta:
        model = Join
        fields = ['email',]

