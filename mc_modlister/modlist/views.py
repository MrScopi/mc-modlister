from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DetailView, ListView
from django.urls import reverse_lazy

from rest_framework.generics import CreateAPIView, ListAPIView

from .forms import ModlistForm
from .models import Modlist
from .serializers import ModlistSerializer

class ModListView(ListView):
    model = Modlist
    template_name = 'modlist/list.html'

class ModCreateAPIView(CreateAPIView):
    queryset = Modlist.objects.all()
    serializer_class = ModlistSerializer

class ModListAPIView(ListAPIView):
    queryset = Modlist.objects.all()
    serializer_class = ModlistSerializer
