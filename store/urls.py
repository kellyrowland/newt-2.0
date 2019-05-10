from django.conf.urls import url
from store.views import *


urlpatterns = [
    url(r'^$', StoreRootView.as_view()),
    url(r'^(?P<store_name>[^/]+)/$', StoreView.as_view()),
    url(r'^(?P<store_name>[^/]+)/perms/$', StorePermView.as_view()),
    url(r'^(?P<store_name>[^/]+)/(?P<obj_id>\d+)/$', StoreObjView.as_view()),
    url(r'^(?P<query>.+)/$', ExtraStoreView.as_view()),
]
    
