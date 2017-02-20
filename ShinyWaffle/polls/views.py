from django.shortcuts import render
from django.http import HttpResponse
import os


def index(request):
    return HttpResponse(os.environ.get("POSTGRES_USER"))


def detail(request, question_id):
    return HttpResponse("You're looking at question {0}".format(question_id))


def results(requestion, question_id):
    return HttpResponse("Results of question {0}".format(question_id))


def vote(request, question_id):
    return
