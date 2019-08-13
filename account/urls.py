from django.urls import path
from account.views import *

urlpatterns = [
    path('host/id/<int:hid>/', HostInfoView.as_view(), name='newt-account-host-id'),
    path('host/<slug:host_name>/', HostInfoView.as_view(), name='newt-account-host-name'),
    path('user/id/<int:uid>/', UserInfoView.as_view(), name='newt-account-user-id'),
    path('user/<slug:user_name>/', UserInfoView.as_view(), name='newt-account-user-name'),
    path('group/id/<int:gid>/', GroupInfoView.as_view(), name='newt-account-group-id'),
    path('group/<slug:group_name>/', GroupInfoView.as_view(), name='newt-account-group-name'),
    path('repo/id/<int:rid>/', RepoInfoView.as_view(), name='newt-account-repo-id'),
    path('repo/<slug:repo_name>/', RepoInfoView.as_view(), name='newt-account-repo-name'),
    path('usage/repo/<slug:repo_name>/', UsageRepoInfoView.as_view(), name='newt-account-usage-repo'),
    path('usage/repo/<slug:repo_name>/users/', UsageRepoInfoView.as_view(), name='newt-account-usage-repo-users'),
    path('usage/user/<slug:user_name>/', UsageUserInfoView.as_view(), name='newt-account-usage-user'),
    path('class/id/<int:cid>/', ClassInfoView.as_view(), name='newt-account-class-id'),
    path('class/<slug:class_name>/', ClassInfoView.as_view(), name='newt-account-class-name'),
    path('office/id/<int:oid>/', OfficeInfoView.as_view(), name='newt-account-office-id'),
    path('office/<slug:office_name>/', OfficeInfoView.as_view(), name='newt-account-office-name'),
    path('organization/id/<int:oid>/', OrgInfoView.as_view(), name='newt-account-org-id'),
    path('organization/<slug:org_name>/', OrgInfoView.as_view(), name='newt-account-org-name'),
    path('person/id/<int:pid>/', PersonInfoView.as_view(), name='newt-account-person-id'),
    path('person/<str:person_name>/', PersonInfoView.as_view(), name='newt-account-person-name'),
    path('program/id/<int:pid>/', ProgramInfoView.as_view(), name='newt-account-program-id'),
    path('program/<str:program_name>/', ProgramInfoView.as_view(), name='newt-account-program-name'),
    path('project/id/<int:pid>/', ProjectInfoView.as_view(), name='newt-account-project-id'),
    path('project/<str:project_name>/', ProjectInfoView.as_view(), name='newt-account-project-name'),
    path('scicat/id/<int:sid>/', ScicatInfoView.as_view(), name='newt-account-scicat-id'),
    path('scicat/<str:scicat_name>/', ScicatInfoView.as_view(), name='newt-account-scicat-name'),
    path('image/id/<int:iid>/photo/', ImageInfoView.as_view(), name='newt-account-image-id'),
    path('image/<str:simage_name>/photo/', ImageInfoView.as_view(), name='newt-account-image-name'),
    path('<str:query>/', GeneralAcctView.as_view()),
]
