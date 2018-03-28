from django.contrib import admin

from voting.models import Votes, VoteDetail

admin.site.register(Votes)
admin.site.register(VoteDetail)
