from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.core import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from .models import Article
from .serializers import ArticleSerializer


@api_view(['GET', 'PUT', 'DELETE'])
def article_detail(request, pk):
    if request.method == 'GET':
        article = get_object_or_404(Article, pk=pk)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        article = get_object_or_404(Article, pk=pk)
        serializer = ArticleSerializer(article, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    
    elif request.method == 'DELETE':
        article = get_object_or_404(Article, pk=pk)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ArticleListAPIView(APIView):
    def get(self, request):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)