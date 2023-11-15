from django.urls import path
from .views import UploadFilesView, Home, SearchView, UserLoginView, LogoutView, ChatView
from . import views

urlpatterns = [
    path('upload_files/', UploadFilesView.as_view(), name='upload_files'),
    path('', Home.as_view(), name='home'),
    path('search/', SearchView.as_view(), name='search'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('chat/', ChatView.as_view(), name='chat'),
]
