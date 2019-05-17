from django.urls import path
from command.views import CommandView, CommandRootView, ExtraCommandView

urlpatterns = [
    path(r'', CommandRootView.as_view()),
    path(r'command/<slug:machine_name>/', CommandView.as_view()),
    path(r'<str:query>/', ExtraCommandView.as_view()),
]
    
