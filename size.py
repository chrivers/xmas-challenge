#!/usr/bin/python
import sys

text = sys.stdin.read()
text = text.replace("\n", "").replace(" ", "")
print "Total: %d characters" % len(text)
