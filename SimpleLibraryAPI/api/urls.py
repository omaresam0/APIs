from django.urls import path
from . import views

# CBV
urlpatterns = [
    path('books/', views.BookCreate.as_view(), name = "book-view-create"),
    path('books/<slug:slug>/', views.BookUpdate.as_view(), name="book-update"),
]

    
