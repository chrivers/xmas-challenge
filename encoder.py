#!/usr/bin/python

import sys

def total_bit_width(string, offset):
    bits = 0
    for c in string:
        bits += len(bin(abs(ord(c) - offset))[2:].lstrip("0"))
    return bits

def best_offset(string):
    best = 0xFFFFFFFF
    index = None
    for x in range(0, 256):
        new = total_bit_width(string, x)
        if new < best:
            best = new
            index = x
    return index

def code(arg):
    print "  ; \"%s\"" % arg.replace("\n", "\\n")
    best = best_offset(arg)
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
