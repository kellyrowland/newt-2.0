from django.urls import path
from job.views import *

urlpatterns = [
    path('', JobRootView.as_view(), name='newt-job'),
    path('<slug:machine>/', JobQueueView.as_view(), name='newt-job-machine'),
    path('<slug:machine>/<int:job_id>/', JobDetailView.as_view(), name='newt-job-machine-jobid'),
    path('<str:query>/', ExtraJobView.as_view()),
]
