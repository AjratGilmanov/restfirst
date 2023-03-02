from django.shortcuts import render,redirect,get_object_or_404
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from .serializers import TaskSerializers
# from .models import Task


class BookListCreateAPIView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
class BookRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


# @api_view(['GET'])
# def apiOverview(request):
#   api_urls = {
#       'List':'/task-list',
#       'Detail View':'/task-detail/<str:pk>/',
#       'Create':'/task-create/',
#       'Update':'/task-update/<str:pk>/',
#       'Delete':'/task-delete/<str:pk>/'
#   }
#   return Response(api_urls)

# @api_view(['POST'])
# def taskCreate(request):
#       serializer = TaskSerializers(data = request.data)
#       if serializer.is_valid():
#           serializer.save()
#       return Response(serializer.data)

# @api_view(['GET'])
# def taskList(request):
#       tasks = Task.objects.all().order_by('-id')
#       serializer = TaskSerializers(tasks, many=True)
#       return Response(serializer.data)

# @api_view(['GET'])
# def taskDetail(request,pk):
#       tasks = Task.objects.get(id=pk)
#       serializer = TaskSerializers(tasks, many = False)
#       return Response(serializer.data)

# @api_view(['POST'])
# def taskUpdate(request, pk):
#       task = Task.objects.get(id=pk)
#       serializer = TaskSerializers(instance=task, data= request.data)

#       if serializer.is_valid():
#             serializer.save()
#       return Response(serializer.data)

# @api_view(['DELETE'])
# def taskDelete(request, pk):
#       task = Task.objects.get(id = pk)
#       task.delete
#       return Response('Удалено!')
