from django.contrib import admin

"""This file defines which Model classes are used in the admin interface"""
from .models import Question, Choice, Vote
admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Vote)
