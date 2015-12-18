#!/usr/bin/python
import sys
filename = sys.argv[1]
text = file(filename).read()
text = text \
       .replace(" ", "") \
       .replace("\t", "") \
       .replace("\n", "") \
       .replace("\r", "") \
       .replace("\f", "") \
       .replace("\v", "")
print "%s: %3d characters" % (filename, len(text))
