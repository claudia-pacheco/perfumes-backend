
from django.urls import path

from brands.views import BrandDetailView, BrandListView


urlpatterns = [
    path("", BrandListView.as_view(), name="creator-list"),
    path("<int:pk>", BrandDetailView.as_view(), name="creator-view"),
]
