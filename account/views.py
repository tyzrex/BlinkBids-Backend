from rest_framework.decorators import api_view
from django.shortcuts import HttpResponse

@api_view(['GET'])
def home(request):
    if request.user.is_authenticated:
        return HttpResponse('You are authenticated ')
    else:
        return HttpResponse('You are not authenticated ')