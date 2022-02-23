from django.contrib.auth.forms import UserCreationForm
from django import forms

from userapp.models import User


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('user_type', 'username', 'email', 'password1', 'password2')
        widgets = {'user_type': forms.HiddenInput}

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


class CompanyUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('company_name', 'partner_image', 'descriptions_company', 'email')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name == 'partner_image':
                field.widget.attrs['class'] = 'custom-file-input'
            else:
                field.widget.attrs['class'] = 'form-control'


class AspirantUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'phone_number', 'city', 'partner_image')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name == 'partner_image':
                field.widget.attrs['class'] = 'custom-file-input'
            else:
                field.widget.attrs['class'] = 'form-control'

    def clean_phone_number(self):
        data = self.cleaned_data['phone_number']
        if data == '':
            return None
        return data
