from core.models import Tournament
from django.shortcuts import get_object_or_404

class DeleteTournamentCommand:
    def __init__(self, tournament_id):
        self.tournament_id = tournament_id

    def execute(self):
        tournament = get_object_or_404(Tournament, id=self.tournament_id)
        tournament.delete()
        return tournament.name
