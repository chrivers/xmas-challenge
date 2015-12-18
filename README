# xmas-challenge

Challenge: Write the smallest possible program (minus whitespace) that
outputs the lyrics to "12 Days of Christmas"

My friend Espen Højsgaard made a public challenge to write the
smallest such program, and these are my contributions to that.

The rules are:

  1. Can't read data files
  2. Must finish in reasonable time
  3. Whitespace characters do not count
  4. The output is case-sensitive

The file full-lyrics.txt contains the lyrics reference. The script
"size.py" takes the name of a file as the first argument, and prints
the number of non-whitespace characters in it.

## xmas1

This is a pure-python implementation that originally wasn't very
small. This is what lead me to persue the other implementations. Since
then, it has become the implementation I'm most proud of. I would be
surprised if a significantly smaller python solution exists.

## xmas2

This slightly bends the rules, since it reads its own source code, but
no external files are used. This is a rather trivial use of zlib
compression to try and minimize the size.

## xmas3

This is a smaller version of xmas2, written in shell code.

## xmas4

This is a python script that does not use any file input at all. It
encodes the lyrics into a string constant consisting of whitespace and
tab (\t), which is then decoded and printed. Since whitespace does not
count, only the decoding logic counts toward the size.

## xmas5

This is a known-minimal solution, which is 0 counted bytes long - it
is implemented entirely in the whitespace programming language,
meaning the whole source file is disregarded.