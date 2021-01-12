from django.contrib import admin
from .models import users, task, score, score_points, achievements, lists, events, prioriry, families, comments

from django import forms
from django.utils.safestring import mark_safe

class taskAdminSite(admin.ModelAdmin):
    actions = ['unsett','sett']
    model = task
    list_display = ("title", "status")
    fields = ['title','task','task_date', 'status', 'points', 'user_id', 'comment_id', 'prioriry_id', 'achievement_id', 'list_id', 'event_id']


    def sett(self, request, queryset):
        """Отметить как выполненные"""
        row_update = queryset.update(status=True)
        if row_update == 1:
            message_bit = "1 запись была обновлена"
        else:
            message_bit = f"{row_update} записей были обновлены"
        self.message_user(request, f"{message_bit}")

    def unsett(self, request, queryset):
        """Отметить как не выполненные"""
        row_update = queryset.update(status=False)
        if row_update == 1:
            message_bit = "1 запись была обновлена"
        else:
            message_bit = f"{row_update} записей были обновлены"
        self.message_user(request, f"{message_bit}")

    unsett.short_description = "Отметить как не выполненные"
    unsett.allowed_permissions = ('change', )

    sett.short_description = "Отметить как выполненные"
    sett.allowed_permissions = ('change',)


admin.site.register(users)
admin.site.register(task, taskAdminSite)
admin.site.register(score)
admin.site.register(score_points)
admin.site.register(achievements)
admin.site.register(lists)
admin.site.register(events)
admin.site.register(prioriry)
admin.site.register(families)
admin.site.register(comments)

