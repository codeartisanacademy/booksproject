from django.shortcuts import render
from django.views.generic import TemplateView

from .models import Book

# Create your views here.
class HomeView(TemplateView):
    template_name = 'home.html'

    def get(self, request):
        return render(request, self.template_name)


class ListView(TemplateView):
    template_name = 'books_list.html'

    def get(self, request):
        books = Book.objects.all()

        return render(request, self.template_name, {'books':books})
