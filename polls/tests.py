import datetime
from django.http import response

from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from .models import Question


def create_question(text, days):
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(text=text, pub_date=time)


class QuestionModelTest(TestCase):

    def test_was_publised_recently_with_old_question(self):
        # was_publised_recently() return False for pub_date older than 1 day
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_question = Question(pub_date=time)
        self.assertIs(old_question.was_published_recently(), False)

    def test_was_publised_recently_with_future_question(self):
        # was_publised_recently() return False for pub_date in the future
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)


class QuestionIndexViewTests(TestCase):

    def test_no_questions(self):
        """
        If no questions exist, an appropriate message is displayed.
        """
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    def test_past_question(self):
        """
        Questions with a pub_date in the past are displayed on the
        index page.
        """
        question = create_question(text="Past question", days=-30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            [question],
        )

    def test_future_question(self):
        """
        Questions with a pub_date in the future aren't displayed on
        the index page.
        """
        question = create_question(text='Future question', days=30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    def test_future_question_and_past_question(self):
        """
        Even if both past and future questions exist, only past questions
        are displayed.
        """
        question = create_question(text="Past question.", days=-30)
        create_question(text="Future question.", days=30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            [question],
        )

    def test_five_past_questions(self):
        """
        The questions index page may display 5 most recent questions.
        """
        question1 = create_question(text="Past question 1.", days=-1)
        question2 = create_question(text="Past question 2.", days=-2)
        create_question(text="Past question 3 (oldest).", days=-30)
        question4 = create_question(text="Past question 4.", days=-4)
        question5 = create_question(text="Past question 5.", days=-5)
        question6 = create_question(text="Past question 6.", days=-6)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            [question1, question2, question4, question5, question6],
        )


    class QuestionDetailViewTest(TestCase):
        
        def test_future_question(self):
            """
            The detail view of a question with a pub_date in the future
            returns a 404 not found.
            """

            future_question = create_question(text='', days=5)
            url = reverse('polls:detail', args=(future_question.id))
            response = self.client.get(url)
            self.assertEqual(response.status_code, 404)

        def test_past_question(self):
            """
            The detail view of a question with a pub_date in the past
            displays the question's text.
            """
            past_question = create_question(text='', days=-1)
            url = reverse('polls:detail', args=(past_question.id))
            response = self.client.get(url)
            self.assertEqual(response.context['latest_question_list'], [past_question])