from __future__ import unicode_literals

from django.db import models
from clipboards.models import Clipboard


class Snippet(models.Model):
	TYPES = (
		('TXT', 'Text'),
		('LNK', 'Link'),
		('IMG', 'Image')
	)
	content = models.TextField()
	clipboard = models.ForeignKey(Clipboard)
	type = models.CharField(max_length=3, default='TXT')

	time_created = models.DateTimeField(auto_now_add=True)
	time_modified = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return '%s' % self.content

