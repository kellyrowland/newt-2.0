from django.urls import path
from status.views import StatusView, ExtraStatusView

urlpatterns = [
    path(r'', StatusView.as_view(), name='newt-status'),
    path(r'<slug:machine_name>/', StatusView.as_view(), name='newt-status-machine'),
    path(r'<str:query>/', ExtraStatusView.as_view()),
]
    
