import datetime
import django.test
from django.urls  import reverse
from django.utils import timezone
from polls.models import Question

class QuestionTests(django.test.TestCase):
    """Test methods of the question class."""

    def test_was_published_recently_with_future_date(self):
        """A question with future pub data should not be published recently"""
        date = timezone.now() + datetime.timedelta(days=1)
        question = Question(question_text="Is this the future?", pub_date=date)
        self.assertFalse( question.was_published_recently() )
        # borderline case
        date = timezone.now() + datetime.timedelta(minutes=1)
        question = Question(question_text="Is this the future?", pub_date=date)
        self.assertFalse( question.was_published_recently() )
        # question with today as start day is recent
        date = timezone.now()
        question = Question(question_text="Is this the present?", pub_date=date)
        self.assertTrue( question.was_published_recently() )

    def test_current_question(self):
        """A question is current if it has been published and not yet closed"""
        date = timezone.now() + datetime.timedelta(minutes=1)
        question = Question(question_text="Is this the future?", pub_date=date)
        self.assertFalse( question.is_current() )
        # question with now as start day is current
        date = timezone.now()
        question = Question(question_text="Is this the present?", pub_date=date)
        self.assertTrue( question.is_current() )
        # question from the distant past, but no closing date
        date = timezone.now() - datetime.timedelta(days=365)
        question = Question(question_text="Is this the present?", pub_date=date)
        self.assertTrue( question.is_current() )
    
class ViewTests(django.test.TestCase):
    """Test the views behave correctly."""

    def setUp(self):
        """initialize test fixture"""
        self.client = django.test.Client()
    
    def test_index_shows_current_poll(self):
        date = timezone.now()
        poll = Question(question_text="Is this the present?", pub_date=date)
        poll.save()
        response = self.client.get( reverse('polls:index'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='polls/index.html')
        # in my code, the list of questions is assigned to context variable 'questions'
        self.assertIn( poll, response.context['questions'] )
   
    def test_index_excludes_future_poll(self):
        """A poll with future pub_date should not be included in the index"""
        date = timezone.now()
        poll = Question(question_text="Is this the present?", pub_date=date)
        poll.save()
        date = timezone.now() + datetime.timedelta(minutes=2)
        future_poll = Question(question_text="Is this the future?", pub_date=date)
        future_poll.save()
        response = self.client.get(reverse('polls:index'))
        self.assertEquals(response.status_code, 200)
        # in my code, the list of questions is assigned to context variable 'questions'
        self.assertIn( poll, response.context['questions'] )
        self.assertNotIn( future_poll, response.context['questions'] )
    
    def test_cannot_access_future_poll(self):
        """Test that a user cannot view poll detail for a future poll."""
        # first verify we can get a current poll
        date = timezone.now()
        poll = Question(question_text="Is this the present?", pub_date=date)
        poll.save()
        url = reverse('polls:detail', args=(poll.pk,))
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
        self.assertContains(response, poll.question_text)
        # now get a future poll
        date = timezone.now() + datetime.timedelta(minutes=2)
        future_poll = Question(question_text="Is this the future?", pub_date=date)
        future_poll.save()
        url = reverse('polls:detail', args=(future_poll.pk,))
        response = self.client.get(url)
        # could be 404 or redirect to index with an error message
        self.assertNotEquals(response.status_code, 200)
       

