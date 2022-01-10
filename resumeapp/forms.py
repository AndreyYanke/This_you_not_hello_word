from django import forms

from resumeapp.models import Resume


class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = (
            'first_name', 'last_name', 'photo', 'sex', 'age', 'citizenship', 'city', 'contact_info', 'ready_to_move', 'position', 'salary',
            'work_schedule','busyness','work_experiences','education', 'about_myself', 'is_publish'
        )


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
