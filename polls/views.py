from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404, HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Questions
from .serializers import QuestionSerializer

## request api and get json back

class questionList(APIView):
    def get(self, request):
        q1 = Questions.objects.all()
        serializer = QuestionSerializer(q1, many=True)
        return Response(serializer.data)
    
    def post(self):
        pass