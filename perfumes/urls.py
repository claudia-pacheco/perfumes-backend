from django.urls import path
from .views import PerfumeDetailView, PerfumeListView

urlpatterns = [
    path('', PerfumeListView.as_view()),
    path('<str:pk>/', PerfumeDetailView.as_view())
]
