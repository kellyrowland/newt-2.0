from newt.views import JSONRestView
from newt.views import AuthJSONRestView
from common.response import json_response
from django.shortcuts import render
from django.conf import settings

import logging
logger = logging.getLogger("newt." + __name__)

from importlib import import_module
acct_adapter = import_module(settings.NEWT_CONFIG['ADAPTERS']['ACCOUNT']['adapter'])

# /api/account/host/<host_name>/
# /api/account/host/id/<hid>/
class HostInfoView(AuthJSONRestView):
    def get(self, request, host_name=None, hid=None):
        return acct_adapter.get_host_info(host_name=host_name, hid=hid)

# /api/account/user/<user_name>/
# /api/account/user/id/<uid>/
class UserInfoView(AuthJSONRestView):
    def get(self, request, user_name=None, uid=None):
        logger.debug("Entering %s:%s" % (self.__class__.__name__, __name__))
        return acct_adapter.get_user_info(user_name=user_name, uid=uid)

# /api/account/group/<group_name>/
# /api/account/group/id/<gid>/
class GroupInfoView(AuthJSONRestView):
    def get(self, request, group_name=None, gid=None):
        return acct_adapter.get_group_info(group_name=group_name, gid=gid)

# /api/account/repo/<repo_name>/
# /api/account/repo/id/<rid>/
class RepoInfoView(AuthJSONRestView):
    def get(self, request, repo_name=None, rid=None):
        return acct_adapter.get_repo_info(repo_name=repo_name, rid=rid)

# /api/account/usage/repo/<repo_name>/
class UsageRepoInfoView(AuthJSONRestView):
    def get(self, request, repo_name=None):
        return acct_adapter.get_usage_repo_info(repo_name=repo_name)

# /api/account/usage/repo/<repo_name>/users/
class UsageRepoUsersInfoView(AuthJSONRestView):
    def get(self, request, repo_name=None):
        return acct_adapter.get_usage_repo_users_info(repo_name=repo_name)

# /api/account/usage/user/<user_name>/
class UsageUserInfoView(AuthJSONRestView):
    def get(self, request, user_name=None):
        return acct_adapter.get_usage_user_info(user_name=user_name)

# /api/account/class/<class_name>/
# /api/account/class/id/<cid>/
class ClassInfoView(AuthJSONRestView):
    def get(self, request, class_name=None, cid=None):
        return acct_adapter.get_class_info(class_name=class_name, cid=cid)

# /api/account/office/<office_name>/
# /api/account/office/id/<oid>/
class OfficeInfoView(AuthJSONRestView):
    def get(self, request, office_name=None, oid=None):
        return acct_adapter.get_office_info(office_name=office_name, oid=oid)

# /api/account/organization/<org_name>/
# /api/account/organization/id/<oid>/
class OrgInfoView(AuthJSONRestView):
    def get(self, request, org_name=None, oid=None):
        return acct_adapter.get_org_info(org_name=org_name, oid=oid)

# /api/account/person/<person_name>/
# /api/account/person/id/<pid>/
class PersonInfoView(AuthJSONRestView):
    def get(self, request, person_name=None, pid=None):
        return acct_adapter.get_person_info(person_name=person_name, pid=pid)

# /api/account/<query>/
class ExtraAcctView(JSONRestView):
    def get(self, request, query):
        return acct_adapter.extras_router(request, query)