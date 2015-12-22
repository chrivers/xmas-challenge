#!/usr/bin/python

import sys

def code(arg):
    if len(arg) > 3:
        for x in reversed(arg):
            print "  push %d" % (ord(x) - ord('a'))
        print ""
        print "  push %d" % len(arg)
        print "  call write_buffer"
    else:
        for x in arg:
            print "  push %d" % ord(x)
            print "  write"

code(sys.argv[1].replace("\\n", "\n"))
