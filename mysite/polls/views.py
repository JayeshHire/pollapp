from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Question, Choice
from django.template import loader
from django.urls import reverse
from django.views import generic
# Create your views here.



#views using predefined behaviour
class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        return Question.objects.order_by("-pub_date")[:5]

class DetailView(generic.DetailView):
    template_name = "polls/detail.html"
    model = Question

class ResultView(generic.DetailView):
    template_name = "polls/result.html"
    model = Question

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    
    try:
        selected_choice = question.choice_set.get(pk=int(request.POST['choice']))
    except (KeyError, Choice.DoesNotExist):
        return render(
            request,
            "polls/detail.html",
            {
                "question":question,
                "error_message":"you didn't select any choice"
            }
        )
    else:
        selected_choice.votes += 1
        selected_choice.save()

        #always return an HttpResponseRedirect after successfully dealing
        #with the post data
        #this prevents data from being posted twice if the user hits back button
        return HttpResponseRedirect(reverse("polls:result",args=(question.id,)))
    

#old views using functions
"""
def index(request):
    question_object_list = Question.objects.order_by("-pub_date")[:5]

    #if the question object list is empty we have to raise an error
    
    #we can use `get_list_or_404(Question, pk= question_id)`
    #function on line 12 is same as calling `Question.objects.filter(pk=1)` and raising Http404(message) if the list is empty 
    
    #we can alternatively use the below line to load the templates
    #template = loader.get_template("polls/index.html")
    
    context = {
        "latest_question_list" : question_object_list
    }
    return render(request, "polls/index.html",context)#"both statements are same" HttpResponse(template.render(context, request))

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    
    #above code is same as the code commented below
    '''
    try:
        question = Question.objects.get(pk=question_id)
        
    except Question.DoesNotExist:
        raise Http404("Quesiton does not exists")
    '''
    
    context = {
            "question" : question
        }
    return render(request, "polls/detail.html",context)

def result(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    #above code is same as below
    '''
    try:
        question = Question.objects.get(pk=question_id)
        choice_list= [choice.choice_text for choice in question.choice_set.all()]
        context = {
            "choice_list":choice_list,
            "question" : question
        }
    except Question.DoesNotExist:
        raise Http404("Question does not exists")
    return render(request, "polls/result.html",context)
    '''
    return render(request, "polls/result.html",{"question":question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    
    try:
        selected_choice = question.choice_set.get(pk=int(request.POST['choice']))
    except (KeyError, Choice.DoesNotExist):
        return render(
            request,
            "polls/detail.html",
            {
                "question":question,
                "error_message":"you didn't select any choice"
            }
        )
    else:
        selected_choice.votes += 1
        selected_choice.save()

        #always return an HttpResponseRedirect after successfully dealing
        #with the post data
        #this prevents data from being posted twice if the user hits back button
        return HttpResponseRedirect(reverse("polls:result",args=(question.id,)))
    '''
    try :
        question = Question.objects.get(pk=question_id)
        choice_list= [choice for choice in question.choice_set.all()]
        context = {
            "choice_list":choice_list,
            "question" : question
        }
    except Question.DoesNotExist:
        raise Http404("Question does not exists")
    '''
    #return render(request, "polls/vote.html",context)


"""