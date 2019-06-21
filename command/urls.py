from django.urls import path
from command.views import CommandView, CommandRootView, ExtraCommandView

urlpatterns = [
    path('', CommandRootView.as_view(), name='newt-command'),
    path('<slug:machine_name>/', CommandView.as_view(), name='newt-command-machine'),
    path('<str:query>/', ExtraCommandView.as_view()),
]
    
