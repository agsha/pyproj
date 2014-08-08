__author__ = 'sgururaj'

import sys
from optparse import *
from utils import call

def do_cov(compile_command, stream, intermediate="intermediate",
           analysis_cmd='/data00/trunk/prevent/objs/linux64/root/bin/cov-analyze-java'):
    call(["/data00/trunk/prevent/objs/linux64/root/bin/cov-build", "--dir", intermediate] + compile_command)
    call([analysis_cmd, "--dir", intermediate])
    call(["/data00/trunk/prevent/objs/linux64/root/bin/cov-commit-defects", "--stream", stream, "--port", "8080",
          "--user", "admin", "--password", "coverity", "--host", "localhost", "--dir", intermediate])


def main():
    usage = "usage: %prog [options] compile_command"
    parser = OptionParser(usage)
    parser.add_option("-s", "--stream", dest="stream",
                      help="commit to this stream [default: %default]", default="udcstream")
    parser.add_option("-i", "--intermediate_dir", dest="intermediate",
                      help="intermediate directory [default: %default]", default="intermediate")
    parser.add_option("-l", "--language", dest="language",
                      help="language of source code. This will decide if cov-analyze or"
                           " cov-analyze-java should be used. correct values "
                           "are 'c' or 'java' [default: %default]", default="java")
    (options, args) = parser.parse_args()
    if len(args) != 1:
        parser.error("incorrect number of arguments")
    if options.language not in ['c', 'java']:
        parser.error("language should be either 'c' or 'java'")

    cmd = '/data00/trunk/prevent/objs/linux64/root/bin/cov-analyze-java'
    if options.language == 'c':
        cmd = '/data00/trunk/prevent/objs/linux64/root/bin/cov-analyze'
    do_cov(args[0].split(" "), options.stream, options.intermediate, cmd)

if __name__ == '__main__':
    main()