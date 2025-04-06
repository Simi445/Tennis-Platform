from django.contrib import admin
from .models import UserProfile, Tournament, Match, Score, TournamentRegistration

admin.site.register(UserProfile)
admin.site.register(Tournament)
admin.site.register(Match)
admin.site.register(Score)
admin.site.register(TournamentRegistration)