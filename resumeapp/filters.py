from django import forms
from django_filters import FilterSet, filters

from resumeapp.models import Resume


class ResumeFilter(FilterSet):

    position = filters.CharFilter(lookup_expr='icontains', label='',
                                  widget=forms.TextInput(attrs={'placeholder': 'Поиск по резюме'}))

    class Meta:
        model = Resume
        fields = ['position']
