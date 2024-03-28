from django.urls import path
from .views import BlogView, BlogDetailView

urlpatterns = [
    path("blogs/", BlogView.as_view(), name="blogs"),
    path("blogs/<int:id>/", BlogDetailView.as_view(), name="blog-detail"),
]