from django.conf.urls import url
from account.views import *

urlpatterns = [
    url(r'^user/(?P<user_name>[^/]+)/$', UserInfoView.as_view()),
    url(r'^user/id/(?P<uid>\d+)/$', UserInfoView.as_view()),
    url(r'^group/(?P<group_name>[^/]+)/$', GroupInfoView.as_view()),
    url(r'^group/id/(?P<gid>\d+)/$', GroupInfoView.as_view()),
    url(r'^(?P<query>.+)/$', ExtraAcctView.as_view()),
]
