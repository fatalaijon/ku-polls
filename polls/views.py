from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.utils import timezone
from .models import Question

"""Views to handle requests to the polls app"""

def index(request):
	"""Show a list of current questions"""
	now = timezone.now()
	# pub_date__lte=now means pub_date() <= now
	questions = Question.objects.filter( pub_date__lte=now )
	context = {'questions': questions, }
	return render(request, 'polls/index.html', context)

def detail(request, question_id):
	"""Return a page showing details of a question"""
	try:
		question = Question.objects.get(pk=question_id)
	except Question.DoesNotExist:
		return Http404(f"Question {question_id} does not exist")
	context = {'question': question}
	return render(request, 'polls/detail.html', context)

def vote(request, question_id):
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
	return HttpResponseRedirect(reverse('polls:result',args=(question_id,)))