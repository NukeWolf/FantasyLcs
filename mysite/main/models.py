from django.db import models
from datetime import datetime
# Create your models here.
class Tutorial(models.Model):
	tutorial_title = models.CharField(max_length=200)
	#Not finite length
	tutorial_content = models.TextField()
	tutorial_published = models.DateTimeField("date published", default=datetime.now())

	def __str__(self):
		return self.tutorial_title

class League(models.Model):
	league_name = models.CharField(max_length=50)
	league_player_size = models.CharField(max_length=50)
	#league_owner = ForeignKey(User)
	leage_team_owners = models.CharField(max_length=50)
	league_teams = models.ForeignKey("Team",on_delete=models.CASCADE)


class Team(models.Model):
	team_name = models.CharField(max_length = 50)
	team_ownerID = models.CharField(max_length=50)
	team_players = models.CharField(max_length=50)
	def __str__(self):
		return self.team_name
