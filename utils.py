__author__ = 'sgururaj'

log_config = {
    'version': 1,
    'formatters': {
        'myformatter': {
            'format': "[PYTHON EXEC] %(name)s %(message)s"
        }
    },
    'handlers': {
        'myhandler': {
            'formatter': 'myformatter',
            'class': 'logging.StreamHandler'
        }
    },
    'root': {
        'level': 'DEBUG',
        'handlers': ['myhandler']
    }
}
import subprocess
import logging
import logging.config
logging.config.dictConfig(log_config)
log = logging.getLogger(__name__)

class Proc(subprocess.Popen):
    def __init__(self, *args, **kwargs):
        log.debug(" ".join(args[0]))
        self._stdout = kwargs.get('stdout', None)
        super(Proc, self).__init__(*args, **kwargs)

    def checked_call(self):
        ret = self.wait()
        if ret != 0:
            raise subprocess.CalledProcessError(ret, " ".join(self.args))

    def capture_output(self):
        if self._stdout != subprocess.PIPE:
            self.kill()
            raise subprocess.CalledProcessError(self.returncode, " ".join(self.args))
        for line in self.stdout:
            yield line.decode("utf8")
