from django.contrib import admin

# Register your models here.
from django.contrib.admin import ModelAdmin

from polls.forms import PollForm
from polls.models import Poll


class PollAdmin(ModelAdmin):

    list_display = ('id', 'title', 'description')
    ordering = ('title', )
    search_fields = ('title', )
    form = PollForm


admin.site.register(Poll, PollAdmin)
