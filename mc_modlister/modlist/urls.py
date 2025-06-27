from django.urls import path

from .views import ModListView, ModCreateAPIView, ModListAPIView, ModDestroyAPIView

urlpatterns = [
    path('', ModListView.as_view(), name='list'),
    path('api/add', ModCreateAPIView.as_view(), name='api_add'),
    path('api/list', ModListAPIView.as_view(), name='api_list'),
    path('api/destroy/<str:pk>', ModDestroyAPIView.as_view(), name='api_remove'),
]
