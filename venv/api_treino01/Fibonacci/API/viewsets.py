from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from Fibonacci.models import Major
from .serializers import Major_Serializer

class Major_ViewSet(ModelViewSet):
    queryset = Major.objects.all()
    serializer_class = Major_Serializer