#!/usr/bin/python
import sys

text = sys.stdin.read()
text = text \
       .replace(" ", "") \
       .replace("\t", "") \
       .replace("\n", "") \
       .replace("\r", "") \
       .replace("\f", "") \
       .replace("\v", "")
print "Total: %d characters" % len(text)
