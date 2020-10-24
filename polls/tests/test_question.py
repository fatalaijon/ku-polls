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
        self.assertFalse( question.can_vote() )
        # question with now as start day is current
        date = timezone.now()
        question = Question(question_text="Is this the present?", pub_date=date)
        self.assertTrue( question.can_vote() )
        # question from the distant past, but no closing date
        date = timezone.now() - datetime.timedelta(days=365)
        question = Question(question_text="Is this the present?", pub_date=date)
        self.assertTrue( question.can_vote() )
