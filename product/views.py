from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.

@api_view(['GET'])
def home(request):
    cats = {'cat1': 'rio', 'cat2': 'dio'}
    return Response(cats) 