#!/usr/bin/python

import sys
import xmas5py

def code(arg):
    print "  ; \"%s\"" % arg.replace("\n", "\\n")
    best = xmas5py.best_offset(arg)
    if len(arg) > 3:
        for x in reversed(arg):
            print "  push %d" % (ord(x) - best)
        print ""
        print "  push %d" % len(arg)
        print "  push %d" % best
        print "  call write_buffer"
    else:
        for x in arg:
            print "  push %d" % ord(x)
            print "  write"

code(sys.argv[1].replace("\\n", "\n"))
