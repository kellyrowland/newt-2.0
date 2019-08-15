import requests
from django.conf import settings
from django.http import Http404, HttpResponseServerError, HttpResponse
from common.response import json_response

def get_data_info(path,username,dirid=None,n=None):
    logger.debug("Datamap")

    url = 'https://portal.nersc.gov/project/datamap/data-'+path+'-json.php?username='+username
    if dirid is not None:
        url += '&dirid='+dirid
        if n is not None:
            url+='&n='+n
    try:
        conn = httplib2.Http(disable_ssl_certificate_validation=True)
        response, content = conn.request(url, 'GET')
        httpstatus = int(response['status'])

    except Exception, e:
        return HttpResponseServerError("Could not connect to REST Service")

    content_type='application/json'
    response = HttpResponse(content, content_type=content_type)
    response['Content-Length'] = len(content)

    return response

def extras_router(request, query):
    for pattern, func, req in patterns:
        match = pattern.match(query)
        if match and req:
            return func(request, **match.groupdict())
        elif match:
            return func(**match.groupdict())

    return json_response(status="Unimplemented", 
                             status_code=501, 
                             error="", 
                             content="query: %s" % query)