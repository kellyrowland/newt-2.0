from django.urls import path
from account.views import *

urlpatterns = [
    path('user/<str:user_name>/', UserInfoView.as_view(), name='newt-account-user-name'),
    path('user/id/<int:uid>/', UserInfoView.as_view(), name='newt-account-user-id'),
    path('group/<slug:group_name>/', GroupInfoView.as_view(), name='newt-account-group-name'),
    path('group/id/<int:gid>/', GroupInfoView.as_view(), name='newt-account-group-id'),
    path('<str:query>/', ExtraAcctView.as_view()),
]
