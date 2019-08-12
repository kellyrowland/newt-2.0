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
        if hid:
            path = "host/id/" + hid + "/"
        elif host_name:
            path = "host/" + host_name + "/"
        return acct_adapter.get_resource(path)

# /api/account/user/<user_name>/
# /api/account/user/id/<uid>/
class UserInfoView(AuthJSONRestView):
    def get(self, request, user_name=None, uid=None):
        logger.debug("Entering %s:%s" % (self.__class__.__name__, __name__))
        if uid:
            path = "user/id/" + uid + "/"
        elif user_name:
            path = "user/" + user_name + "/"
        return acct_adapter.get_resource(path)

# /api/account/group/<group_name>/
# /api/account/group/id/<gid>/
class GroupInfoView(AuthJSONRestView):
    def get(self, request, group_name=None, gid=None):
        if gid:
            path = "group/id/" + gid + "/"
        elif group_name:
            path = "group/" + group_name + "/"
        return acct_adapter.get_resource(path)

# /api/account/repo/<repo_name>/
# /api/account/repo/id/<rid>/
class RepoInfoView(AuthJSONRestView):
    def get(self, request, repo_name=None, rid=None):
        if rid:
            path = "repo/id/" + rid + "/"
        elif repo_name:
            path = "repo/" + repo_name + "/"
        return acct_adapter.get_resource(path)

# /api/account/usage/repo/<repo_name>/
class UsageRepoInfoView(AuthJSONRestView):
    def get(self, request, repo_name=None):
        path = "repo/" + repo_name + "/"
        return acct_adapter.get_usage(path)

# /api/account/usage/repo/<repo_name>/users/
class UsageRepoUsersInfoView(AuthJSONRestView):
    def get(self, request, repo_name=None):
        path = "repo/" + repo_name + "/users/"
        return acct_adapter.get_usage(path)

# /api/account/usage/user/<user_name>/
class UsageUserInfoView(AuthJSONRestView):
    def get(self, request, user_name=None):
        path = "user/" + user_name + "/"
        return acct_adapter.get_usage(path)

# /api/account/class/<class_name>/
# /api/account/class/id/<cid>/
class ClassInfoView(AuthJSONRestView):
    def get(self, request, class_name=None, cid=None):
        if cid:
            path = "class/id/" + cid + "/"
        elif class_name:
            path = "class/" + class_name + "/"
        return acct_adapter.get_resource(path)

# /api/account/office/<office_name>/
# /api/account/office/id/<oid>/
class OfficeInfoView(AuthJSONRestView):
    def get(self, request, office_name=None, oid=None):
        if oid:
            path = "office/id/" + oid + "/"
        elif office_name:
            path = "office/" + office_name + "/"
        return acct_adapter.get_resource(path)

# /api/account/organization/<org_name>/
# /api/account/organization/id/<oid>/
class OrgInfoView(AuthJSONRestView):
    def get(self, request, org_name=None, oid=None):
        if oid:
            path = "organization/id/" + oid + "/"
        elif org_name:
            path = "organization/" + org_name + "/"
        return acct_adapter.get_resource(path)

# /api/account/person/<person_name>/
# /api/account/person/id/<pid>/
class PersonInfoView(AuthJSONRestView):
    def get(self, request, person_name=None, pid=None):
        if pid:
            path = "person/id/" + pid + "/"
        elif person_name:
            path = "person/" + person_name + "/"
        return acct_adapter.get_resource(path)

# /api/account/program/<program_name>/
# /api/account/program/id/<pid>/
class ProgramInfoView(AuthJSONRestView):
    def get(self, request, program_name=None, pid=None):
        if pid:
            path = "program/id/" + pid + "/"
        elif program_name:
            path = "program/" + program_name + "/"
        return acct_adapter.get_resource(path)

# /api/account/project/<project_name>/
# /api/account/project/id/<pid>/
class ProjectInfoView(AuthJSONRestView):
    def get(self, request, project_name=None, pid=None):
        if pid:
            path = "project/id/" + pid + "/"
        elif project_name:
            path = "project/" + project_name + "/"
        return acct_adapter.get_resource(path)

# /api/account/scicat/<scicat_name>/
# /api/account/scicat/id/<sid>/
class ScicatInfoView(AuthJSONRestView):
    def get(self, request, scicat_name=None, sid=None):
        if sid:
            path = "scicat/id/" + sid + "/"
        elif scicat_name:
            path = "scicat/" + scicat_name + "/"
        return acct_adapter.get_resource(path)

# /api/account/<query>/
class GeneralAcctView(JSONRestView):
    def get(self, request, query):
        return acct_adapter.get_resource(query)
