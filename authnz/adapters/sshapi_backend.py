import logging
import requests
from django.contrib.auth.models import User 
from django.core.exceptions import ObjectDoesNotExist
from django.conf import settings

from authnz.models import Cred

logger = logging.getLogger(__name__)

class SSHAPIBackend:
    
    # implement this
    # 
    def authenticate(self, username=None, password=None, request=None):
        logger.debug('authenticate "%s"' %username)
        try:
            s = requests.Session()
            response = s.post(settings.SSHPROXY_SERVER,
            		  		  auth=(username,password))
            response.raise_for_status()
        except Exception as e:
            logger.debug("SSH API Exception: %s" % e) 
            return None

        credentials = response.text
        if not credentials:
        	return None

        try:
            myuser = User.objects.get(username=username)
        except ObjectDoesNotExist:
            # This isn't actually used anywhere, but you might make this smarter
            email = "%s@%s" % (username, settings.NEWT_DOMAIN)
            try:
                myuser = User.objects.create_user(username, email)
            except Exception as ex:
                logger.error(ex)
                raise ex

		mycred = Cred(key=credentials, user=myuser)
		mycred.save()
        myuser.backend = 'django.contrib.auth.backends.ModelBackend'
        return myuser
  
    def get_user(self, user_id):
        """Returns User object, throws User.DoesNotExist
        """
        logger.debug("get_user %d " %(user_id))
        try:
            return User.objects.get(pk=user_id)
        except ObjectDoesNotExist:
            return None