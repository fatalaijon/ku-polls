"""Entities in the polls application"""
import datetime
from django.db import models
# a date that's compabible with Django DateTimeField
from django.utils import timezone

class Question(models.Model):
    """A poll question with some text, starting date, and closing date"""
    question_text = models.CharField(max_length=80)
    pub_date = models.DateTimeField('poll starting date')

    def __str__(self):
        """string representation of a question"""
        return self.question_text

    def was_published_recently(self) -> bool:
        """Return true if question was published in the last 1 day."""
        start_date = timezone.now() - datetime.timedelta(days=1)
        now = timezone.now()
        return self.pub_date >= start_date and self.pub_date <= now
    
    def is_current(self) -> bool:
        """Query if this question has publication date before now"""
        now = timezone.now()
        return self.pub_date <= now

class Choice(models.Model):
    """A possible answer to a poll question"""
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=80)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
	
