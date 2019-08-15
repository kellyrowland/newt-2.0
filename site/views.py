from newt.views import JSONRestView
from newt.views import AuthJSONRestView
from common.response import json_response
from django.shortcuts import render
from django.conf import settings

import logging
logger = logging.getLogger("newt." + __name__)

from importlib import import_module
site_adapter = import_module(settings.NEWT_CONFIG['ADAPTERS']['SITE']['adapter'])

# only needs username
class DataUsageView(AuthJSONRestView):
    def get(self, request, username):
        logger.debug("Entering %s:%s" % (self.__class__.__name__, __name__))
        path = 'mgt'
        return site_adapter.get_data_info(path, username=username)

# needs username, directory, number of files
class UserLargestFilesView(AuthJSONRestView):
    def get(self, request, username, dirid=None, n=None):
        logger.debug("Entering %s:%s" % (self.__class__.__name__, __name__))
        path = 'user'
        return site_adapter.get_data_info(path, username=username, dirid=dirid, n=n)

# needs username, directory, number of files
class UserOldestFilesView(AuthJSONRestView):
    def get(self, request, username, dirid=None, n=None):
        logger.debug("Entering %s:%s" % (self.__class__.__name__, __name__))
        path = 'user-oldest'
        return site_adapter.get_data_info(path, username=username, dirid=dirid, n=n)

class ExtraSiteView(JSONRestView):
    def get(self, request, query):
        return site_adapter.extras_router(request, query)
