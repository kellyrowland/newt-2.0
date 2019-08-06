import logging
import requests
import os
from django.contrib.auth.models import User 
from django.core.exceptions import ObjectDoesNotExist
from django.conf import settings

logger = logging.getLogger("newt." + __name__)

class SSHAPIBackend:
    
    def authenticate(self, request, username=None, password=None):
        logger.debug('authenticate "%s"' % (username))
        try:
            key, cert = self._authenticate(settings.SSHPROXY_SERVER,
                                             username, password)
        except:
            logger.debug("Login failed for: %s" % username)
            raise
            return AnonymousUser()
        try:
            myuser = User.objects.get(username=username)
        except ObjectDoesNotExist:
            logger.debug('No record of username "%s"' %username)
            email = ''
            try:
                myuser = User.objects.create_user(username, email)
            except Exception as ex:
                logger.error(ex)
                traceback.print_exc()
                raise
            logger.debug('calling update_user signal')
            try:
                signals.update_user.send(sender=self, user=myuser)
                # signals.update_user_groups.send(sender=self, user=myuser)
            except Exception as ex:
                logger.error(ex)
        return myuser

    def get_user(self, user_id):
        """Returns User object, throws User.DoesNotExist
        """
        logger.debug("get_user %d " % (user_id))
        try:
            return User.objects.get(pk=user_id)
        except ObjectDoesNotExist:
            return None

    def _write_key(self, file, data):
        key = data
        cert = None
        with open(file, 'w') as f:
            f.write(data)
        os.chmod(file, 0o600)
        # out = check_output(["ssh-keygen","-f",file,'-y'])
        # with open(file+'.pub','w') as f:
        #     f.write(str(out, 'utf-8'))
        for line in data.split('\n'):
            if line.startswith('ssh-rsa-cert'):
                logger.debug(line)
                with open(file+'-cert.pub', 'w') as f:
                    f.write(line)
                    cert = line
        return key, cert

    def _authenticate(self, server, username, pwd, skey='', cert_path='/tmp'):
        """Authenticate with SSH Auth API, and return the private key
        if login is successful.
        Return None otherwise.
        """

        key = None
        cert = None
        try:
            if skey != '':
                data = json.dumps({'skey': skey})
                r = requests.post(server, data=data, auth=(username, pwd))
            else:
                r = requests.post(server, auth=(username, pwd))
            if r.status_code == 200:
                file = '%s/%s.key' % (cert_path, username)
                key, cert = self._write_key(file, r.text)
            else:
                logger.warning("SSH Auth API Authentication failed (%s@%s):",
                                 username, server)
                return None
        except:
            logger.warning("SSH Auth API Authentication failed: ")
            return None
        else:
            return key, cert