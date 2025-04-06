import csv
from django.http import HttpResponse

class ExportMatchesCSVCommand:
    def __init__(self, matches, scores):
        self.matches = matches
        self.scores = scores

    def execute(self):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="matches.csv"'

        writer = csv.writer(response)
        writer.writerow([
            'Tournament', 'Player 1', 'Player 2', 'Referee',
            'Date', 'Location', 'Player 1 Score', 'Player 2 Score'
        ])

        for match in self.matches:
            score = self.scores.get(match.id)
            writer.writerow([
                match.tournament.name,
                match.player1.username,
                match.player2.username,
                match.referee.username if match.referee else "N/A",
                match.date,
                match.location,
                score.player1_score if score else '',
                score.player2_score if score else ''
            ])

        return response
