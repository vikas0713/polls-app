from django.contrib import admin

# Register your models here.
from django.contrib.admin import ModelAdmin

from polls.models import Poll


class PollAdmin(ModelAdmin):

    list_display = ('id', 'title', 'description')
    ordering = ('title', )
    search_fields = ('title', )


admin.site.register(Poll, PollAdmin)
