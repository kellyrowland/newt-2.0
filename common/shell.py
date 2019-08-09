from subprocess import PIPE, run
import shlex

import logging
import signal
from django.utils.encoding import smart_str


logger = logging.getLogger("newt." + __name__)


class Alarm(Exception):
    pass


def alarm_handler(signum, frame):
    raise Alarm


# initialization code
try:
    signal.signal(signal.SIGALRM, alarm_handler)
except ValueError as e:
    logger.warning('setting alarm handler failed: "%s"' % e)

def run_command(command, env=None, timeout=600):
    args = shlex.split(smart_str(command))
    try:
        p = run(args, stdout=PIPE, stderr=PIPE, env=env, timeout=timeout)
        output = p.stdout
        error = p.stderr
        retcode = p.returncode
        logger.debug(p)
        return (output, error, retcode)
    except OSError as ex:
        logger.error('running command failed: "%s", OSError "%s"' % (' '.join(args), ex))
        raise ex

    return (output, error, retcode)

def run_ssh_command(command, machine_name, env=None, timeout=600):
    flags = " -q -o StrictHostKeyChecking=no -i %s -l %s" % (self.credfilename,
                                                             self.user.username)
    command = '%s %s %s %s' % (_settings.SSH_CMD, flags, machine_name, command)
    (output, error, retcode) = run_command(command)

    return (output, error, retcode)
