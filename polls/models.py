"""Entities in the polls application"""

from django.db import models

class Question(models.Model):
    """A poll question with some text, starting date, and closing date"""
    question_text = models.CharField(max_length=80)
    pub_date = models.DateTimeField('poll starting date')

    def __str__(self):
        """string representation of a question"""
        return self.question_text
    


class Choice(models.Model):
    """A possible answer to a poll question"""
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=80)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
	
