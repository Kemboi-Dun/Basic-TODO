from django.shortcuts import render

from rest_framework import viewsets
from .models import Todo
from .serializers import TodoSerializer

# Create your views here.
class TodoViewSet(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()