from django.urls import path
from account.views import *

urlpatterns = [
    path('user/<slug:user_name>/', UserInfoView.as_view()),
    path('user/id/<int:uid>/', UserInfoView.as_view()),
    path('group/<slug:group_name>/', GroupInfoView.as_view()),
    path('group/id/<int:gid>/', GroupInfoView.as_view()),
    path('<str:query>/', ExtraAcctView.as_view()),
]
