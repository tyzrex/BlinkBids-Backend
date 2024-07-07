from rest_framework.decorators import api_view
from django.shortcuts import HttpResponse
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from .models import User as CustomUser
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken
from .serializers import UserLoginSerializer
@api_view(['GET'])
def home(request):
    if request.user.is_authenticated:
        return HttpResponse('You are authenticated ')
    else:
        return HttpResponse('You are not authenticated ')
    


@api_view(["GET"])
def get_user_from_jwt(request):
    token = request.META.get("HTTP_AUTHORIZATION")

    if token is None:
        return Response(status=HTTP_400_BAD_REQUEST)
    token_obj = AccessToken(token.split(" ")[1])

    user_queryset = CustomUser.objects.filter(id=token_obj["user_id"])
    if not user_queryset.exists():
        return Response(status=HTTP_400_BAD_REQUEST)
    user = user_queryset.values("first_name", "email").first()
    serializer = UserLoginSerializer(user)

    return Response(serializer.data, status=HTTP_200_OK)
