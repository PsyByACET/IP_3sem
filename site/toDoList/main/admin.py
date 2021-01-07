from django.contrib import admin
from .models import users, task, score

admin.site.register(users)
admin.site.register(task)
admin.site.register(score)

