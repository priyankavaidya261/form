from django.db import models


class Snippet(models.Model):
	name = models.CharField(max_length=100)
	body = models.TextField()

	def _str_(self):
		return self.name