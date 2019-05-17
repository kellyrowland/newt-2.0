from django.urls import path
from status.views import StatusView, ExtraStatusView

urlpatterns = [
    path(r'', StatusView.as_view()),
    path(r'status/<slug:machine_name>/', StatusView.as_view()),
    path(r'<str:query>/', ExtraStatusView.as_view()),
]
    
