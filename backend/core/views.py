from django.shortcuts import render
from django.http import HttpResponse
from .serializers import PostSerializer

from .models import Post
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets 
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from .permissions import AdminOrReadOnly,IsOwnerOrReadOnly

 
# Create your views here.

class BlogViewset(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes= [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
 