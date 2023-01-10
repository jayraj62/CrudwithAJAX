from django import forms
from .models import Userinfo
class UserForm(forms.ModelForm):
    class Meta:
        model=Userinfo
        fields='__all__'    