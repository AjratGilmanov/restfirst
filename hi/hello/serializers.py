from rest_framework import serializers
from .models import Book
# from .models import Task
# class TaskSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = Task
#         fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'