from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse

from .models import Question

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = dict(
        latest_question_list=latest_question_list,
    )
    return render(request, 'index.html', context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)  
    return render(request, 'detail.html', dict(
        question=question,
    ))


def results(request, question_id):
    response = f"You're looking at the result of question {question_id}"
    return HttpResponse(response)


def vote(request, question_id):
    return HttpResponse(f"You're voting on question {question_id}")