from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Question
from django.template import loader

def index(request):
    # return HttpResponse("You're on the index page")
    latest_question_list =  Question.objects.order_by("-pub_date")[:5]
    # output = ", ".join([q.question_text for q in latest_question_list])
    # return HttpResponse(output)
    # template = loader.get_template("polls/index.html")
    context = {
        "latest_question_list": latest_question_list,
        }
    return render(request, "polls/index.html", context)


def detail(request, question_id):
    # return HttpResponse("You're looking at question %s."%question_id)
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})
    
def vote(request, question_id):
    return HttpResponse("You're voting on question %s."%question_id)

def results(request, question_id):
    return HttpResponse("You're looking at the resutls of question %s."%question_id)
