from django.http import HttpResponse

class ExportMatchesTXTCommand:
    def __init__(self, matches, scores):
        self.matches = matches
        self.scores = scores

    def execute(self):
        response = HttpResponse(content_type='text/plain')
        response['Content-Disposition'] = 'attachment; filename="matches.txt"'

        for match in self.matches:
            score = self.scores.get(match.id)
            response.write(
                f"{match.tournament.name}: {match.player1.username} vs {match.player2.username} "
                f"on {match.date.strftime('%Y-%m-%d %H:%M')} at {match.location} | "
                f"Referee: {match.referee.username if match.referee else 'N/A'} | "
                f"Score: {score.player1_score if score else ''}-{score.player2_score if score else ''}\n"
            )

        return response
