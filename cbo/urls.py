from django.urls import path
from .views import UploadFilesView, Home, SearchView
from . import views

urlpatterns = [
    path('upload_files/', UploadFilesView.as_view(), name='upload_files'),
    path('', Home.as_view(), name='home'),
    path('search/', SearchView.as_view(), name='search'),
]
