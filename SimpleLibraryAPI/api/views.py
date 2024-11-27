from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Book
from .serializers import BookSerializer

# --- CBV ---
class BookCreate(APIView):   
    def get(self, request, *args, **kwargs):
        # Retrieve all books
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        # Create a new book
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        # Delete all books
        Book.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Custom View for Retrieving, Updating, and Deleting a specific book
class BookUpdate(APIView):
    def get_object(self, slug):
        # Retrieve a specific book by pk
        try:
            return Book.objects.get(slug=slug)
        except Book.DoesNotExist:
            return None

    def get(self, request, slug, *args, **kwargs):
        # If book exists, serialize it. else, Not Found
        book = self.get_object(slug)
        if not book:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = BookSerializer(book)
        return Response(serializer.data)

    def put(self, request, slug, *args, **kwargs):
        # Update a specific book
        book = self.get_object(slug)
        if not book:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, slug, *args, **kwargs):
        # Delete a specific book
        book = self.get_object(slug)
        if not book:
            return Response(status=status.HTTP_404_NOT_FOUND)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# --- FBV ---

# @api_view(['GET', 'POST', 'DELETE'])
# def BookCreate(request):
#     if request.method == 'GET':
#         # Retrieve all books
#         books = Book.objects.all()
#         serializer = BookSerializer(books, many=True)
#         return Response(serializer.data)
    
#     elif request.method == 'POST':
#         # Create a new book
#         serializer = BookSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         # Delete all books
#         Book.objects.all().delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# @api_view(['GET', 'PUT', 'DELETE'])
# def BookUpdate(request, pk):
#     try:
#         book = Book.objects.get(pk=pk)
#     except Book.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         # Retrieve a specific book
#         serializer = BookSerializer(book)
#         return Response(serializer.data)

#     elif request.method == 'PUT':
#         # Update a specific book
#         serializer = BookSerializer(book, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         # Delete a specific book
#         book.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# --- Simple One with ---

# # GET, CREATE 
# class BookCreate(generics.ListCreateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#     # DELETE ALL Objs
#     def delete(self, request, *args, **kwargs):
#         Book.objects.all().delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# # GET, UPDATE, DELETE
# class BookUpdate(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#     lookup_field = "pk"
