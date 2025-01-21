from django.shortcuts import render
from rest_framework import generics
from .serializers import BookSerializer
from .models import Books


class BooksListCreate(generics.ListCreateAPIView):
    queryset = Books.objects.all()
    serializer_class = BookSerializer
    
    
    

