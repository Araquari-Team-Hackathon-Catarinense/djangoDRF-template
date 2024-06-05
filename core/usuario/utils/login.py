from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.utils.translation import gettext_lazy as _
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from django.contrib.auth import authenticate, get_user_model
import json
from drf_spectacular.utils import extend_schema
User = get_user_model()

@extend_schema(tags=['Usuario'])
@api_view(['POST'])
@authentication_classes([])
@permission_classes([AllowAny]) 
def get_user(request):
    data = json.loads(request.body.decode('utf-8'))
    email = data.get("email", '')
    password = data.get("password", '')
    print(email, password)
    if email is not None and password is not None:
        try:
            user = User.objects.get(email=email)
            user = authenticate(email=email, password=password)
        except User.DoesNotExist:
            user = None   
    else:
        return Response(
            {"message": "Credenciais inválidas!"}, status=status.HTTP_400_BAD_REQUEST
        )
    print(user)
    if user is not None:
        refresh = RefreshToken.for_user(user)
        access = AccessToken.for_user(user)
        response_data = {
            "refresh": str(refresh),
            "access": str(access),
            "username": user.username,
            "email": user.email,
            "id": user.id,
            "message": "Login realizado com sucesso!"
        }
        return Response(response_data, status=status.HTTP_200_OK)
    else:
          return Response(
            {"message": "Credenciais inválidas!"}, status=status.HTTP_400_BAD_REQUEST
        )