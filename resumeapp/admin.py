from django.contrib import admin

from resumeapp.models import Resume, Work_expirience, Education, Citizenship


class ResumeAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'position',)
    list_filter = ('position',)
    exclude = ('groups', 'user_permissions')


admin.site.register(Resume, ResumeAdmin)
admin.site.register(Work_expirience)
admin.site.register(Education)
admin.site.register(Citizenship)