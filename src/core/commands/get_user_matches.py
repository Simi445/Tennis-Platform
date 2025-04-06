from core.models import Match

def get_matches_for_user(user):
    matches = []
    role = user.userprofile.role

    if role == 'referee':
        match_list = Match.objects.filter(referee=user)
    elif role == 'player':
        match_list = Match.objects.all()
    else:
        match_list = []

    for match in match_list:
        matches.append({
            'tournament': match.tournament.name,
            'player1': match.player1.username,
            'player2': match.player2.username,
            'date': match.date,
            'location': match.location,
        })

    return matches
