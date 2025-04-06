from core.models import Tournament
from django.shortcuts import get_object_or_404
from django.utils.dateparse import parse_date

class SaveTournamentCommand:
    def __init__(self, data):
        self.data = data

    def execute(self):
        tournament_id = self.data.get("tournament_id")
        name = self.data.get("name")
        location = self.data.get("location")
        start_date = parse_date(self.data.get("start_date"))
        end_date = parse_date(self.data.get("end_date"))

        if tournament_id:
            tournament = get_object_or_404(Tournament, id=tournament_id)
        else:
            tournament = Tournament()

        tournament.name = name
        tournament.location = location
        tournament.start_date = start_date
        tournament.end_date = end_date
        tournament.save()

        return tournament
