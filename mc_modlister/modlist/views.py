from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DetailView, ListView
from django.urls import reverse_lazy

from .forms import ModlistForm
from .models import Modlist

class ModListView(ListView):
    model = Modlist
    template_name = 'modlist/list.html'

class ModCreateView(CreateView):
    form = ModlistForm
    template_name = 'modlist/add.html'
