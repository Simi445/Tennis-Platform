from django.shortcuts import get_object_or_404
from core.models import Match, Score

class UpdateScoreCommand:
    def __init__(self, match_id, player1_score, player2_score):
        self.match_id = match_id
        self.player1_score = player1_score
        self.player2_score = player2_score

    def execute(self):
        match = get_object_or_404(Match, id=self.match_id)
        score, _ = Score.objects.update_or_create(
            match=match,
            defaults={
                'player1_score': self.player1_score,
                'player2_score': self.player2_score,
            }
        )
        return score
