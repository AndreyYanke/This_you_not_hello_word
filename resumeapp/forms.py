from django import forms
from django.db.models import TextField

from resumeapp.models import Resume, ResponseAspirant
from this_you_not_hello_word import config


class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = '__all__'
        widgets = {'user': forms.HiddenInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

class ResponseAspirantForm(forms.ModelForm):
    class Meta:
        model = ResponseAspirant
        fields = '__all__'


