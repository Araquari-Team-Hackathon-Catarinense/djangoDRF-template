from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.utils.translation import gettext_lazy as _
from rest_framework import status
from ..models import Usuario
from drf_spectacular.utils import extend_schema


@extend_schema(tags=['Usuario'])
@api_view(["POST"])
@authentication_classes([])
@permission_classes([AllowAny])
def create_user(request):
    email = request.data.get("email")
    password = request.data.get("password")

    if Usuario.objects.filter(email=email).exists():
        return Response({"error": "Email já cadastrado"}, status=status.HTTP_400_BAD_REQUEST)
    if email and password:
        user = Usuario.objects.create(
            email=email,
        )
        user.set_password(password)
        user.save()
        return Response({"success": "Usuário criado com sucesso"}, status=status.HTTP_201_CREATED)