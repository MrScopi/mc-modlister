from django.urls import path

from .views import ModListView, ModCreateView

urlpatterns = [
    path('', ModListView.as_view(), name='list'),
    path('add/', ModCreateView.as_view(), name='add'),
]
