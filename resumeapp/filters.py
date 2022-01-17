from django import forms
from django_filters import FilterSet, filters

from resumeapp.models import Resume
from userapp.models import City


class ResumeFilter(FilterSet):

    position = filters.CharFilter(lookup_expr='icontains', label='',
                                  widget=forms.TextInput(attrs={'placeholder': 'Поиск по резюме'}))

    city = filters.ModelChoiceFilter(queryset=City.objects.all(), label='Город:')

    class Meta:
        model = Resume
        fields = ['position', 'city']
