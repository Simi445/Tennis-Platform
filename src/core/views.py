from django.shortcuts import redirect,render,get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from core.utils.factories import create_user_with_role
from django.template.context_processors import request
from core.models import Tournament, TournamentRegistration,Match,Score
from django.utils.dateparse import parse_date
from django.contrib import messages
from django.db.models import Q

#We import our command pattern classes
from core.commands.update_score import UpdateScoreCommand
from core.commands.get_match_list import GetMatchListCommand
from core.commands.delete_tournament import DeleteTournamentCommand
from core.commands.save_tournament import SaveTournamentCommand
from core.commands.edit_user import EditUserCommand
from core.commands.delete_user import DeleteUserCommand
from core.commands.register_for_tournament import RegisterForTournamentCommand
from core.commands.available_tournaments import AvailableTournamentsQuery
from core.commands.update_email import UpdateEmailCommand
from core.commands.update_password import UpdatePasswordCommand
from core.commands.get_user_matches import get_matches_for_user
from core.commands.register_user import RegisterUserCommand
from core.commands.login_user import LoginUserCommand
from django.http import HttpResponse
from core.models import Match, Score
from core.commands.csv_export_command import ExportMatchesCSVCommand
from core.commands.txt_export_command import ExportMatchesTXTCommand

def export_matches(request):
    export_format = request.GET.get('format')
    matches = Match.objects.select_related('tournament', 'player1', 'player2', 'referee')
    scores = {s.match_id: s for s in Score.objects.all()}

    command = None
    if export_format == 'csv':
        command = ExportMatchesCSVCommand(matches, scores)
    elif export_format == 'txt':
        command = ExportMatchesTXTCommand(matches, scores)

    if command:
        return command.execute()

    return HttpResponse("Invalid format", status=400)


def login_view(request, *args, **kwargs):
    if request.method == "POST":
        cmd = LoginUserCommand(request)
        if cmd.execute():
            return redirect('land_page')
        return render(request, "login.html", {"error": cmd.error})

    return render(request, "login.html")




def register_view(request, *args, **kwargs):
    if request.method == "POST":
        cmd = RegisterUserCommand(request)
        success = cmd.execute()
        if success:
            return redirect("land_page")
        return render(request, "login.html", {"error": cmd.error})

    return render(request, "login.html")



def main_view(request, *args, **kwargs):
    user = request.user
    user_profile = user.userprofile
    all_users = User.objects.select_related('userprofile').all()

    userObject = {
        'username': user.username,
        'email': user.email,
        'role': user_profile.role,
    }

    matches = get_matches_for_user(user)

    return render(request, "landing_page.html", {
        'user': userObject,
        'users': all_users,
        'matches': matches
    })


def profile_view(request):
    user = request.user
    profile = user.userprofile

    success_message = ""
    error_message = ""

    if request.method == "POST":
        if 'new_email' in request.POST:
            cmd = UpdateEmailCommand(user, request.POST.get("new_email"), request.POST.get("confirm_email"))
            if cmd.execute():
                success_message = "Email updated successfully!"
            else:
                error_message = cmd.error

        elif 'new_password' in request.POST:
            cmd = UpdatePasswordCommand(
                user,
                request.POST.get("current_password"),
                request.POST.get("new_password"),
                request.POST.get("confirm_password"),
            )
            if cmd.execute(request):
                success_message = "Password changed successfully!"
            else:
                error_message = cmd.error

    return render(request, "profile.html", {
        "user": user,
        "user_type": profile.role,
        "success_message": success_message,
        "error_message": error_message,
    })



def tournaments_view(request):
    query = AvailableTournamentsQuery(request.user)
    available_tournaments = query.fetch()

    return render(request, 'tournaments.html', {
        'tournaments': available_tournaments,
    })


def register_for_tournament(request, tournament_id):
    RegisterForTournamentCommand(request.user, tournament_id).execute()
    return redirect('tournaments')


def delete_user(request, user_id):
    if request.method == "POST":
        DeleteUserCommand(user_id).execute()
        return redirect('land_page')
    user = get_object_or_404(User, id=user_id)
    return render(request, 'landing_page.html', {'user': user})


def edit_user_submit(request):
    if request.method == "POST":
        EditUserCommand(request.POST).execute()
        return redirect('land_page')

def save_tournament(request):
    if request.method == "POST":
        SaveTournamentCommand(request.POST).execute()
        messages.success(request, "Tournament saved successfully.")
    return redirect('tournaments')


def delete_tournament(request, tournament_id):
    if request.method == "POST":
        deleted_name = DeleteTournamentCommand(tournament_id).execute()
        messages.success(request, f"Tournament '{deleted_name}' deleted successfully.")
    return redirect('tournaments')

def match_list(request):
    data = GetMatchListCommand(request.user).execute()
    return render(request, 'matches.html', {**data, 'user': request.user})


def update_score(request):
    if request.method == 'POST':
        cmd = UpdateScoreCommand(
            match_id=request.POST.get('match_id'),
            player1_score=request.POST.get('player1_score'),
            player2_score=request.POST.get('player2_score')
        )
        cmd.execute()
    return redirect('match_management')