from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DetailView, ListView
from django.urls import reverse_lazy

from rest_framework.generics import CreateAPIView, ListAPIView, DestroyAPIView, UpdateAPIView

from .models import TrackedMods
from .serializers import TrackedModsSerializer

class ModListView(ListView):
    model = TrackedMods
    template_name = 'modlist/list.html'

class ModCreateAPIView(CreateAPIView):
    queryset = TrackedMods.objects.all()
    serializer_class = TrackedModsSerializer

class ModListAPIView(ListAPIView):
    queryset = TrackedMods.objects.all()
    serializer_class = TrackedModsSerializer

class ModDestroyAPIView(DestroyAPIView):
    queryset = TrackedMods.objects.all()
    serializer_class = TrackedModsSerializer
