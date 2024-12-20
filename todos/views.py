from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Todo
from .serializers import TodoSerializer

class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
