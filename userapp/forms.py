from django.contrib.auth.forms import UserCreationForm
from django import forms

from userapp.models import User


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class AspirantRegisterForm(RegisterForm):
    class Meta(RegisterForm.Meta):
        model = User
        fields = ('first_name', 'last_name') + RegisterForm.Meta.fields


class CompanyRegisterForm(RegisterForm):
    class Meta(RegisterForm.Meta):
        model = User
        fields = ('company_name',) + RegisterForm.Meta.fields


