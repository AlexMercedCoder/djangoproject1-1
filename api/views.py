from .models import Dog
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import DogSerializer


class DogViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Dog.objects.all()
    serializer_class = DogSerializer
    permission_classes = [permissions.AllowAny] #Coule be [permissions.IsAuthenticated]
