from django.urls import path
from .views import UploadFilesView, Home
from . import views

urlpatterns = [
    path('upload_files/', UploadFilesView.as_view(), name='upload_files'),
    path('', Home.as_view(), name='home'),
]
