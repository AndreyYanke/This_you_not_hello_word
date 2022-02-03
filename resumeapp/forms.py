from django import forms

from resumeapp.models import Resume, ResponseAspirant


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
