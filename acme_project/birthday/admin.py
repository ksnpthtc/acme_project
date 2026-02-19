from django.contrib import admin

from .models import Birthday


class BirthdayAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'first_name',
        'second_name',
        'birthday')
    list_editable = (
        'first_name',
        'second_name',
        'birthday')
    list_filter = (
        'second_name',
        'birthday'
    )


admin.site.register(Birthday, BirthdayAdmin)