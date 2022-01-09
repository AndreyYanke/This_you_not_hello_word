from django.contrib.auth.forms import UserCreationForm
from django import forms

from userapp.models import User


class AspirantRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('user_type', 'username', 'first_name', 'last_name', 'email', 'password1', 'password2')
        widgets = {'user_type': forms.HiddenInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class CompanyRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('user_type', 'username', 'company_name', 'email', 'password1', 'password2')
        widgets = {'user_type': forms.HiddenInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
