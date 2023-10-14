from django.urls import path
from .views import UploadFilesView
from . import views

urlpatterns = [
    path('upload_files/', UploadFilesView.as_view(), name='upload_files'),
    path('', views.home, name='home'),
]
