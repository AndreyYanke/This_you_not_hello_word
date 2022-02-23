from django.contrib import admin
from vacancyapp.models import Vacancy, KeySkill


class VacancyAdmin(admin.ModelAdmin):
    list_display = ('name','is_active' )

    ordering = ('is_active',)


admin.site.register(Vacancy, VacancyAdmin)
admin.site.register(KeySkill)
