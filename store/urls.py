from django.urls import path
from store.views import *

urlpatterns = [
    path(r'', StoreRootView.as_view(),name='newt-store'),
    path(r'<slug:store_name>/', StoreView.as_view(), name='newt-store-name'),
    path(r'<slug:store_name>/perms/', StorePermView.as_view(), name='newt-store-perms'),
    path(r'<slug:store_name>/<int:obj_id>/', StoreObjView.as_view(), name='newt-store-name-id'),
    path(r'<str:query>/', ExtraStoreView.as_view()),
]
