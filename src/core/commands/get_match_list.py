from django.contrib.auth.models import User
from core.models import Match, Score, Tournament
from django.db.models import Q

class GetMatchListCommand:
    def __init__(self, user):
        self.user = user

    def execute(self):
        username = self.user.username
        user_profile = self.user.userprofile

        matches = Match.objects.select_related('tournament', 'player1', 'player2', 'referee').filter(
            Q(referee__username__icontains=username) |
            Q(player1__username__icontains=username) |
            Q(player2__username__icontains=username) |
            Q(tournament__name__icontains=username) |
            Q(location__icontains=username)
        )

        tournaments = Tournament.objects.all()
        players = User.objects.filter(userprofile__role='player')
        referees = User.objects.filter(userprofile__role='referee')

        scores = Score.objects.select_related('match')
        score_map = {score.match_id: score for score in scores}

        for match in matches:
            match.score = score_map.get(match.id)

        return {
            "matches": matches,
            "tournaments": tournaments,
            "players": players,
            "referees": referees,
        }
