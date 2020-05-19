from django.shortcuts import render
from django.http import HttpResponse
from .models import Question

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.") #questo fa visualizzare il messaggio Hello, world. You're at the polls index. 
    # quando si digita l'indirizzo http://127.0.0.1:8000/polls/

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # output = ', '.join([q.question_text for q in latest_question_list])
    # return HttpResponse(output)
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))