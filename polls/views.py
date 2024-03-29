from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404, HttpResponse, HttpResponseRedirect
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Questions, Choice
from .serializers import QuestionSerializer, ChoiceSerializer

from django.views import generic

## request api and get json back

class questionList(APIView):
    def get(self, request):
        q1 = Questions.objects.all()
        serializer = QuestionSerializer(q1, many=True)
        return Response(serializer.data)
    
    def post(self):
        pass
    
    
class choiceList(APIView):
    def get(self, request):
        c1 = Choice.objects.all()
        serializer = ChoiceSerializer(c1, many=True)
        return Response(serializer.data)
    
    def post(self):
        pass
    
    
class IndexView(APIView):
    def get(self, request):
        q1 = Questions.objects.all()
        serializer = QuestionSerializer(q1, many=True)
        return Response(serializer.data)
    
    def post(self):
        pass
    
# Create your views here.
# class IndexView(generic.ListView):
#     # template_name = 'polls/index.html'
#     context_object_name = 'latest_question_list'

    # def get_queryset(self):
    #     """Return the last five published questions."""
    #     return Question.objects.order_by('-pub_date')[:5]


# class DetailView(generic.DetailView):
#     model = Question
#     template_name = 'polls/detail.html'


# class ResultsView(generic.DetailView):
#     model = Question
#     template_name = 'polls/results.html'
    
    
    
    
# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     context = {'latest_question_list': latest_question_list}
#     return render(request, 'polls/index.html', context)
# def detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/detail.html', {'question': question})

# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.html', {'question': question})




# def vote(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     try:
#         selected_choice = question.choice_set.get(pk=request.POST['choice'])
#     except (KeyError, Choice.DoesNotExist):
#         # Redisplay the question voting form.
#         return render(request, 'polls/detail.html', {
#             'question': question,
#             'error_message': "You didn't select a choice.",
#         })
#     else:
#         selected_choice.votes += 1
#         selected_choice.save()
#         # Always return an HttpResponseRedirect after successfully dealing
#         # with POST data. This prevents data from being posted twice if a
#         # user hits the Back button.
#         return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))