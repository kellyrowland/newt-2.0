from django.urls import path
from store.views import *

urlpatterns = [
    path(r'', StoreRootView.as_view()),
    path(r'store/<slug:store_name>/', StoreView.as_view()),
    path(r'store/<slug:store_name>/perms/', StorePermView.as_view()),
    path(r'store/<slug:store_name>/<int:obj_id>/', StoreObjView.as_view()),
    path(r'<str:query>/', ExtraStoreView.as_view()),
]
