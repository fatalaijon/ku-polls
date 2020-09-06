from django.contrib import admin

"""This file defines which Model classes are used in the admin interface"""
from .models import Question, Choice
admin.site.register(Question)
admin.site.register(Choice)
