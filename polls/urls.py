"""Mapping of http request paths to handlers (views)"""
from django.urls import path
from . import views
from . import class_views

# define a namespace for url names.  
# This name is used to qualify names in the {% url %} and reverse() functions.
# So you would write '{% url polls:index %}' instead of '{% url index %}' 
app_name = 'polls'

urlpatterns = [
	path("",                  class_views.IndexView.as_view(), name='index'),
	path('<int:pk>/',         views.detail, name='detail'),
	path('<int:pk>/results/', class_views.ResultsView.as_view(), name='results'),
	path('<int:pk>/vote/',    views.vote, name='vote'),
]
