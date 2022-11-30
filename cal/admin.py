from django.contrib import admin

from .models import Form


class FormAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'assignee', 'city', 'sched_on')
    list_filter = ('city', 'assignee', 'sched_on')
    search_fields = ('city', 'assignee')


admin.site.register(Form, FormAdmin)
