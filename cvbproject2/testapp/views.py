from django.shortcuts import render
from django.views.generic import ListView,DetailView
from testapp.models import Books
# Create your views here.
# for only listview
class bookslistview(ListView):
    model=Books
    template_name='testapp/books.html'
    context_object_name="books"    #model
class bookslistview2(ListView):
    model=Books
    template_name='testapp/books.html'
    context_object_name="books"
# for only detailview for perticular record we use   default 
class bookdetailview(DetailView): 
    model=Books
    template_name='testapp/books_details.html'
    context_object_name="books"

    