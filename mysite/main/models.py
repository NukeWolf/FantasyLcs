from django.db import models
from datetime import datetime
from django.contrib.auth.forms import User
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator
from .validators import TeamNameValidator

# Create your models here.
class Tutorial(models.Model):
	tutorial_title = models.CharField(max_length=200)
	#Not finite length
	tutorial_content = models.TextField()
	tutorial_published = models.DateTimeField("date published", default=datetime.now())

	def __str__(self):
		return self.tutorial_title

class League(models.Model): 
	league_name = models.CharField(max_length=50,unique=True)
	league_player_size = models.IntegerField(validators=[MaxValueValidator(8),MinValueValidator(4)])
	league_owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,default='')#,default=User.objects.get(username='nukewolf'))
	league_teams = models.ManyToManyField("Team")
	league_is_drafted = models.BooleanField(default=False)
	def __str__(self):
		return self.league_name



class Team(models.Model):
	team_name = models.CharField(max_length=50,validators=TeamNameValidator(team_name))
	team_owner = models.ForeignKey(get_user_model(),on_delete=models.CASCADE,default='')#,default=User.objects.get(username='nukewolf'))
	top = models.CharField(max_length=50)
	jng = models.CharField(max_length=50)
	mid = models.CharField(max_length=50)
	bot = models.CharField(max_length=50)
	sup = models.CharField(max_length=50)
	flex = models.CharField(max_length=50)
	team = models.CharField(max_length=50,default=1)
	bn1 = models.CharField(max_length=50)
	bn2 = models.CharField(max_length=50)
	bn3 = models.CharField(max_length=50)
	wins = models.CharField(max_length=50)
	loss = models.CharField(max_length=50)
	tie = models.CharField(max_length=50)
	def __str__(self):
		return self.team_name
