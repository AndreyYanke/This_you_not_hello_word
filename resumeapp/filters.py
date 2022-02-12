from django import forms
from django.db.models import Q
from django_filters import FilterSet, filters

from resumeapp.models import Resume
from userapp.models import City


class ResumeFilter(FilterSet):


    position = filters.CharFilter(lookup_expr='icontains', label='', method='name_or_company_name_filter',
                              widget=forms.TextInput(attrs={'placeholder': 'Поиск по резюме','class':'form-control'}))

    city = filters.ModelChoiceFilter(queryset=City.objects.all(), label='Город:',widget=forms.Select(attrs={'class':'form-control'}))


    class Meta:
        model = Resume
        fields = ['position', 'city']

    def name_or_company_name_filter(self, queryset, name, value):
        position = self.data.get('position')
        city = self.data.get('city')
        return queryset.filter(Q(position__icontains=value) | Q(user__company_name__icontains=value))
