from django.contrib import admin

from polls.models import Question, Options

admin.site.register(Question)
admin.site.register(Options)
