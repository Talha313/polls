from django.shortcuts import render,get_object_or_404
from django.http import  HttpResponse,HttpResponseRedirect

from django.urls import reverse
# Create your views here.
from .models import Question
from django.template import RequestContext
def index(request):
    latest_question = Question.objects.order_by('-pub_date')[:5]

    context={'latest_question':latest_question}

  #  output= ", ".join(a.Question_text for a in latest_question)
  #  return render(request,'polls/index.html',{})
    return render(request , 'polls/index.html' , context)
def detail(requset, question_id):
    question=get_object_or_404(Question , pk=question_id)
    return render(requset,'polls/detail.html', {'q':question},question_id)
    #return  Htt("This is detail view of question: %s" % question_id)
def result(request , question_id):
    q=get_object_or_404(Question, pk=question_id)
    return  render(request, 'polls/result.html', {'question':q})

def vote (request, question_id):
    q=get_object_or_404(Question,pk=question_id)
    try:
        selected_choice=q.choices_set.get(pk=request.POST['choices'])
    except:
        return render(request , 'polls/detail.html' , {'question':q ,'error_message':"plz select a choice "} )
    else:
        selected_choice.votes +=1
        selected_choice.save()

    return HttpResponseRedirect(reverse('polls:result', args=(q.id,)))