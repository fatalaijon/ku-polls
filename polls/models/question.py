"""Entities in the polls application"""
import datetime
from django.db import models
# a date that's compabible with Django DateTimeField
from django.utils import timezone


class Question(models.Model):
    """A poll question with some text, starting date, and closing date."""
    question_text = models.CharField(max_length=80)
    pub_date = models.DateTimeField('poll starting date')
    end_date = models.DateTimeField('poll closing date', null=True)

    def __str__(self):
        """string representation of a question"""
        return self.question_text

    def was_published_recently(self) -> bool:
        """Return true if question was published in the last 1 day."""
        start_date = timezone.now() - datetime.timedelta(days=1)
        now = timezone.now()
        return self.pub_date >= start_date and self.pub_date <= now
        
    def can_vote(self) -> bool:
        """Query if voting is currently allowed for this question"""
        now = timezone.now()
        if self.pub_date > now:
            return False
        # if no closing date then voting allowed indefinitely
        if not self.end_date:
            return True
        return now <= self.end_date

    def is_published(self) -> bool:
        """Query if this question has publication date before now."""
        now = timezone.now()
        return self.pub_date <= now

