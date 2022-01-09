from django.contrib import admin
from userapp.models import User, City


class UserAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'user_type')
    list_filter = ('user_type',)
    exclude = ('groups', 'user_permissions')


admin.site.register(User, UserAdmin)
admin.site.register(City)
