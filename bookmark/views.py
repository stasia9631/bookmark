from django.shortcuts import render
from django.views.generic.list import ListView

from .models import Bookmark

class BookmarkListView(ListView):
    model = Bookmark

from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

class BookmarkCreateView(CreateView):
    model = Bookmark
    fields = ['site_name','url']
    success_url = reverse_lazy('list')
    template_name_suffix = '_create'

from django.views.generic.detail import DetailView

class BookmarkDetailView(DetailView):
    model = Bookmark

# Create your views here.
