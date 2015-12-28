from __future__ import unicode_literals

from django.db import models


class Clipboard(models.Model):
	SCOPES = (
		('PR', 'Private'),
		('PU', 'Public'),
		('LM', 'Limited')
	)

	name = models.CharField(max_length=50)
	scope = models.CharField(max_length=2, choices=SCOPES)
	color = models.CharField(max_length=7)

	time_created = models.DateTimeField(auto_now_add=True)
	time_modified = models.DateTimeField(auto_now=True)

	def __str__(self):
		return '%s' % (self.name)