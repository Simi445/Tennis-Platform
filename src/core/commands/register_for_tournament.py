from django.shortcuts import get_object_or_404
from core.models import Tournament, TournamentRegistration

class RegisterForTournamentCommand:
    def __init__(self, user, tournament_id):
        self.user = user
        self.tournament_id = tournament_id

    def execute(self):
        tournament = get_object_or_404(Tournament, id=self.tournament_id)
        TournamentRegistration.objects.get_or_create(player=self.user, tournament=tournament)
