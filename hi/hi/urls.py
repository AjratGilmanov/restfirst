from django.urls import path
from hello.views import BookListCreateAPIView, BookRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('books/', BookListCreateAPIView.as_view(), name='book_list_create_api'),
    path('books/<int:pk>/', BookRetrieveUpdateDestroyAPIView.as_view(), name='book_retrieve_update_destroy_api'),
]