from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import os


def index(request):
    latest_question_list = ["quest1", "quest2", "quest3", "quest4", "quest5"]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))


def detail(request, question_id):
    return HttpResponse("{0} looking at question {1}".format(
                os.environ.get("POSTGRES_USER"),
                question_id))


def results(request, question_id):
    return HttpResponse("Results of question {0}".format(question_id))


def vote(request, question_id):
    return HttpResponse("Voting on question {0}".format(question_id))
