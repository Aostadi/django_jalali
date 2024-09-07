from Users.models import CustomUser
from django.contrib import admin


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'gender', 'national_code', 'birthday_date')
    search_fields = ('username', 'full_name')
    ordering = ('ceremony_datetime',)
    def first_name(self, obj):
        return obj.get_first_and_last_name()['first_name']
    def last_name(self, obj):
        return obj.get_first_and_last_name()['last_name']
admin.site.register(CustomUser, CustomUserAdmin)

