"""Views that extend Django Generic Views.
   These can be used instead of function views to reduce coding,
   but it helps to know what the views are doing "behind the scenes".
"""
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.utils import timezone
from django.views import generic

from .models import Choice, Question

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'questions'
    # queryset = Question.objects.filter(...)

    def get_queryset(self):
        """Return all published questions, sorted by pub_date"""
        now = timezone.now()
        return Question.objects.filter(pub_date__lte=now).order_by('-pub_date')
    
class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'
    context_object_name = 'question'

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'
    context_object_name = 'question'
