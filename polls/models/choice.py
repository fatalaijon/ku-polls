"""Entities in the polls application"""
import datetime
from django.db import models
# a date that's compabible with Django DateTimeField
from django.utils import timezone
from .question import Question


class Choice(models.Model):
    """A possible answer to a poll question."""
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=80)
    votes = models.IntegerField(default=0)

    class Meta:
        ordering = ['choice_text']

    def __str__(self):
        return self.choice_text
	
