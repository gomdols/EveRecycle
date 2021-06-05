from post.serializers import BoardSerializer
from post.models import Board
from django.shortcuts import render
from rest_framework import generics



def index(request):
    return render(request, 'post/index.html')



class ListBoard(generics.ListCreateAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer

class DetailBoard(generics.RetrieveUpdateDestroyAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer
