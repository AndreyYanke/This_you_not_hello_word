from django import forms
from django.db.models import Q
from django_filters import FilterSet, filters

from userapp.models import City
from vacancyapp.models import Vacancy


class VacancyFilter(FilterSet):

    name = filters.CharFilter(lookup_expr='icontains', label='', method='name_or_company_name_filter',
                              widget=forms.TextInput(attrs={'placeholder': 'Профессия, должность или компания'}))

    city = filters.ModelChoiceFilter(queryset=City.objects.all())

    class Meta:
        model = Vacancy
        fields = ['name', 'city']

    def name_or_company_name_filter(self, queryset, name, value):
        return queryset.filter(Q(name__icontains=value) | Q(user__company_name__icontains=value))
