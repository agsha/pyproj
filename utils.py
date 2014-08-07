__author__ = 'sgururaj'

import subprocess


def call(cmd):
    print ("[ PYTHON_EXEC ]" + " ".join(cmd))
    process = subprocess.Popen(cmd, bufsize=-1)
    ret = process.wait()
    if ret != 0:
        raise subprocess.CalledProcessError(ret, cmd)



def call_capture(cmd):
    print (" ".join(cmd))
    process = subprocess.Popen(cmd, bufsize=-1, stdout=subprocess.PIPE)
    for line in process.stdout.readline():
        yield line.decode("utf8")

