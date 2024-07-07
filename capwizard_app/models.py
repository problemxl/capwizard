from django.db import models

class Team(models.Model):
    name = models.CharField(max_length=200)
    team_id = models.IntegerField()
    city = models.CharField(max_length=200)
    venue = models.CharField(max_length=200)

    def __str__(self):
        return self.name

# Create your models here.
class Player(models.Model):
    name = models.CharField(max_length=200)
    team = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    points = models.IntegerField()
    assists = models.IntegerField()
    rebounds = models.IntegerField()
    steals = models.IntegerField()
    blocks = models.IntegerField()
    turnovers = models.IntegerField()
    fg_percentage = models.FloatField()
    ft_percentage = models.FloatField()
    three_percentage = models.FloatField()
    minutes = models.IntegerField()
    games_played = models.IntegerField()
    fantasy_points = models.FloatField()

    def __str__(self):
        return self.name