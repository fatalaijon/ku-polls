"""Mapping of http request paths to handlers (views)"""
from django.urls import path
from . import views

# define a namespace for urls.  Used in lookups via '{% url name %}'
app_name = 'polls'

urlpatterns = [
	path("", views.index, name='index'),
	path('<int:question_id>/',         views.detail, name='detail'),
	#path('<int:question_id>/results/', views.results, name='results'),
	path('<int:question_id>/vote/',    views.vote, name='vote'),
]
