"""Entities in the polls application"""
import datetime
from django.db import models
import django.contrib.auth.models
# a date that's compabible with Django DateTimeField
from django.utils import timezone
# import modules instead of names from modules to avoid circular import error
from .question import Question


class Choice(models.Model):
    """A possible answer to a poll question."""
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=80)
    #votes = models.IntegerField(default=0)

    class Meta:
        ordering = ['choice_text']

    def __str__(self):
        return self.choice_text
	
    @property
    def votes(self):
        """"Return the number of votes for this choice."""
        return Vote.objects.filter(choice=self).count()


class Vote(models.Model):
    """A vote by a user for one choice (answer) to a poll Question."""
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)
    user = models.ForeignKey(
            django.contrib.auth.models.User,
            null=False,
            blank=False,
            on_delete=models.CASCADE
            )

    def __str__(self):
       return f"Vote by {self.user.username} for choice {self.choice.id} on question {self.choice.question}"
