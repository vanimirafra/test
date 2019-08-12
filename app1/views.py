# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from app1.serializers import BooksSerializer
from app1.models import Books
from django.shortcuts import get_object_or_404


class BooksListView(APIView):
    def get(self, request):
        book=Books.objects.all()
        serializer=BooksSerializer(book, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer=BooksSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print(serializer)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BooksDetailView(APIView):
    def get(self, request, pk):
        book = get_object_or_404(Books, pk=pk)
        serializer = BooksSerializer(book)
        return Response(serializer.data)


    def put(self, request, pk):
        book = get_object_or_404(Books, pk=pk)
        serializer = BooksSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        book = get_object_or_404(Books, pk=pk)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


'''def home(request):
    if request.method == 'POST':
        print(request.POST)
        b = Books(title=request.POST['title'],pages= request.POST['pages'])
        b.save()
        context = {'books': Books.objects.all()}
        return render(request, 'test.html', context)


    else :

        context = {"books": Books.objects.all()}
        return render(request, 'test.html', context)'''


'''def home(request):
      return redirect(reverse('home'))
def index(request):
      return HttpResponse('<h1>hi</h1>')'''     
