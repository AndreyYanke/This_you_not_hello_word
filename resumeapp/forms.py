from django import forms

from resumeapp.models import Resume, ResponseAspirant
from userapp.models import User


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



class ResumeUser(forms.ModelForm):
    user = forms.ModelChoiceField(queryset=User.objects.all().select_related(), label='user', required=False)
    class Meta:
        model = User
        fields = '__all__'


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

        # service_pools = ServicePool.objects.values_list('id', 'name')
        # self.fields['service_pools'].choices = service_pools