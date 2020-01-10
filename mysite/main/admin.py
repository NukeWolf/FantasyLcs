from django.contrib import admin
from .models import Tutorial, League,Team
# Register your models here.

class TutorialAdmin(admin.ModelAdmin):
	#Changes order of the fields
	# fields = ["tutorial_title",
	#  		  "tutorial_published",
	#  		  "tutorial_content"]


	#Groups them together
	fieldsets = [
		("Title/date",{"fields": ["tutorial_title", "tutorial_published"]}),
		("Content", {"fields":["tutorial_content"]})
	]
class LeagueAdmin(admin.ModelAdmin):
	fields = ["league_name","league_player_size","league_owner","league_teams","league_is_drafted"]
class TeamAdmin(admin.ModelAdmin):
	fields = ["team_name","team_owner","top","jng",'mid','bot','sup']




admin.site.register(Tutorial,TutorialAdmin)
admin.site.register(Team,TeamAdmin)
admin.site.register(League,LeagueAdmin)
