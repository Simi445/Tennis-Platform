from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.db import models
from django.core.validators import MinValueValidator

class UserProfile(models.Model):
    ROLE_CHOICES = (
        ('player', 'Tennis Player'),
        ('referee', 'Referee'),
        ('admin', 'Administrator'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

class Tournament(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()

class Match(models.Model):
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    player1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='player1_matches')
    player2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='player2_matches')
    referee = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='referee_matches')
    date = models.DateTimeField()
    location = models.CharField(max_length=100)

class Score(models.Model):
    match = models.OneToOneField(Match, on_delete=models.CASCADE)
    player1_score = models.PositiveIntegerField(validators=[MinValueValidator(0)])
    player2_score = models.PositiveIntegerField(validators=[MinValueValidator(0)])


class TournamentRegistration(models.Model):
    player = models.ForeignKey(User, on_delete=models.CASCADE)
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    registered_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('player', 'tournament')  #ca sa fie unic!