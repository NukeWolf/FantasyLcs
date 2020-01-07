from django.contrib import admin
from .models import Tutorial
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

admin.site.register(Tutorial,TutorialAdmin)