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


def run_command(command, machine_name, env=None, timeout=600):
    command = "ssh -t " + machine_name + " " + command
    args = shlex.split(smart_str(command))
    try:
        p = run(args, stdout=PIPE, stderr=PIPE, env=env, timeout=timeout)
        output = p.stdout.decode("utf-8")
        error = p.stderr.decode("utf-8")
        retcode = p.returncode
        return (output, error, retcode)
    except OSError as ex:
        logger.error('running command failed: "%s", OSError "%s"' % (' '.join(args), ex))
        raise ex

    return (output, error, retcode)
