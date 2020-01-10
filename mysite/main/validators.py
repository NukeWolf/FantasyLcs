from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
def TeamNameValidator(teams,name):
	for team in teams:
		if team.team_name == name:
			raise ValidationError(
            _('A team in this league has used the same name'),)
