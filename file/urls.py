from django.urls import path
from file.views import FileView, FileRootView, FilePathView, ExtraFileView

urlpatterns = [
    path('', FileRootView.as_view(), name='newt-file'),
    path('<slug:machine_name>/', FileView.as_view(), name='newt-file-machine'),
    path('<slug:machine_name>/<path:path>/', FilePathView.as_view(), name='newt-file-machine-path'),
    path('<str:query>/', ExtraFileView.as_view()),
]
    
