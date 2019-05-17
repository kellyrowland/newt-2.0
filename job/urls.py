from django.urls import path
from job.views import *

urlpatterns = [
    path(r'', JobRootView.as_view()),
    path(r'job/<slug:machine>/', JobQueueView.as_view()),
    path(r'job/<slug:machine>/<int:job_id>/', JobDetailView.as_view()),
    path(r'<str:query>/', ExtraJobView.as_view()),
]
