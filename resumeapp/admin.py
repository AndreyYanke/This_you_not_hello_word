from django.contrib import admin

from resumeapp.models import Resume, Work_expirience, Education, Citizenship, ResponseAspirant, ResponseCompany, \
    FollowerAspirant


class ResumeAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'position', 'is_publish')
    list_filter = ('position',)
    exclude = ('groups', 'user_permissions')
    ordering = ('is_publish',)


admin.site.register(Resume, ResumeAdmin)
admin.site.register(Work_expirience)
admin.site.register(Education)
admin.site.register(Citizenship)
admin.site.register(ResponseAspirant)
admin.site.register(ResponseCompany)
admin.site.register(FollowerAspirant)
