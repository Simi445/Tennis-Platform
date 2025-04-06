from core.models import Tournament, TournamentRegistration

class AvailableTournamentsQuery:
    def __init__(self, user):
        self.user = user

    def fetch(self):
        registered_ids = TournamentRegistration.objects.filter(
            player=self.user
        ).values_list('tournament_id', flat=True)
        return Tournament.objects.exclude(id__in=registered_ids)
