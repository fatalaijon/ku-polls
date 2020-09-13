from django.contrib import messages
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import redirect, render, reverse
from django.utils import timezone
from .models import Question, Choice

"""Views to handle requests to the polls app"""

def index(request):
	"""Show a list of published poll questions"""
	now = timezone.now()
	# pub_date__lte=now means pub_date() <= now
	questions = Question.objects.filter( pub_date__lte=now )
	context = {'questions': questions, }
	return render(request, 'polls/index.html', context)

def detail(request, pk):
	"""
	Return a page showing details of a question, with choices.
	
	Arguments:
		pk = the question id (primary key)
	"""
	question_id = pk
	try:
		question = Question.objects.get(pk=question_id)
	except Question.DoesNotExist:
		return Http404(f"Question {question_id} does not exist")
	# don't display poll if not published yet
	if question.pub_date > timezone.now():
		# use Django's messages framework. Requires index page to show the message.
		messages.error(request, f"Question {question_id} is not available")
		return redirect("polls:index")
	context = {'question': question}
	return render(request, 'polls/detail.html', context)

def vote(request, pk):
	"""
	Record a vote for a poll question. The selected choice is in the POST body.
	
	Arguments:
		pk = the question id (primary key)
	"""
	question_id = pk
	# lookup the question
	try:
		question = Question.objects.get(pk=question_id)
	except Question.DoesNotExist:
		return Http404(f"Question {question_id} does not exist")
	if not question.is_current():
		return HttpResponse("Voting not allowed for that question", status=403)
	# get the user's choice
	try:
		choice_id = request.POST['choice']
	except KeyError:
		context = {'question': question, 
		    'error_message': "You didn't select a valid choice"}
		return render(request, 'polls/detail.html', context)
	try:
		selected_choice = question.choice_set.get(pk=choice_id)
	except Choice.DoesNotExist:
		context = {'question': question, 
		    'error_message': "You didn't select a valid choice"}
		return render(request, 'polls/detail.html', context)
	# record the vote
	selected_choice.votes += 1
	selected_choice.save()
	return HttpResponseRedirect(reverse('polls:results',args=(question_id,)))

def results(request, pk):
	"""Show the voting results for a poll question"""
	question_id = pk
	try:
		question = Question.objects.get(pk=question_id)
	except Question.DoesNotExist:
		return Http404(f"Question {question_id} does not exist")
	if not question.is_published():
		return HttpResponse("Voting not allowed for that question", status=403)
	context = {'question': question}
	return render(request, 'polls/results.html', context)