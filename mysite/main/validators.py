from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
class TeamNameValidator:
	def __init__(self, limit_value, message=None):
		self.limit_value = limit_value
		if message:
			self.message = message

	def __call__(self, value):
		cleaned = self.clean(value)
		limit_value = self.limit_value() if callable(self.limit_value) else self.limit_value
		params = {'limit_value': limit_value, 'show_value': cleaned, 'value': value}
		if self.compare(cleaned, limit_value):
			raise ValidationError(self.message, code=self.code, params=params)

	def __eq__(self, other):
		return (
			isinstance(other, self.__class__) and
			self.limit_value == other.limit_value and
			self.message == other.message and
			self.code == other.code
		)

	def compare(self, a, b):
		for team in a:
			if (team == b):
				return True
		return False

	def clean(self, x):
		print(League.objects.get(league_name=x).league_teams)
		return League.objects.get(league_name=x).league_teams
		
