from django.conf.urls import url
from job.views import *

urlpatterns = [
    url(r'^$', JobRootView.as_view()),
    url(r'^(?P<machine>[^/]+)/$', JobQueueView.as_view()),
    url(r'^(?P<machine>[^/]+)/(?P<job_id>[^/]+)/$', JobDetailView.as_view()),
    url(r'^(?P<query>.+)/$', ExtraJobView.as_view()),
]
    
