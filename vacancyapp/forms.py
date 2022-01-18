from django import forms

from vacancyapp.models import Vacancy


class VacancyForm(forms.ModelForm):
    class Meta:
        model = Vacancy
        exclude = ('is_active', )
        widgets = {'user': forms.HiddenInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
