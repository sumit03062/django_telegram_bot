from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth.models import User
from .serializers import PublicSerializer, UserSerializer
from .tasks import send_welcome_email

@api_view(["GET"])
@permission_classes([AllowAny])
def public_api(request):
    return Response({"message": "This is a public API!"})

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def protected_api(request):
    serializer = UserSerializer(request.user)
    return Response(serializer.data)
