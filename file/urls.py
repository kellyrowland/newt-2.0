from django.urls import path
from file.views import FileView, FileRootView, ExtraFileView

urlpatterns = [
    path(r'', FileRootView.as_view()),
    path(r'file/<slug:machine_name>/<str:path>/', FileView.as_view()),
    path(r'<str:query>/', ExtraFileView.as_view()),
]
    
