from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import redirect, render, reverse
from django.utils import timezone
from polls.models import Question, Choice, Vote

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

@login_required
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
    if not question.can_vote():
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
    # Does user already have a Vote for this question?
    vote = get_vote_for_user(request.user, question)
    if not vote:
        vote = Vote(user=request.user, question=question, choice=selected_choice)
    else:
        # change an existing vote
        vote.choice = selected_choice
    vote.save()
    return HttpResponseRedirect(reverse('polls:results',args=(question_id,)))

def get_vote_for_user(user, poll_question):
    """Find and return an existing vote for a user on a poll question."""
    try:
        # vote.question is 
        votes = Vote.objects.filter(user=user).filter(question=poll_question)
    except Votes.DoesNotExist:
        return None
    if len(votes) == 0:
        return None
    if len(votes) > 1:
        logger = logging.getLogger(__name__)
        logger.error(f"user {user} has {len(votes)} votes for poll {poll_question.question_text}")
        for vote in votes:
            logger.error(str(vote))
    return votes[0]  

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
