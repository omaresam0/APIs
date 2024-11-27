from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    published_date = serializers.DateTimeField(format="%Y-%m-%d")  # Define the format you want
    class Meta:
        model = Book
        fields = '__all__'