import re
from StringIO import StringIO

re_comment = re.compile("\s*;.*")
re_push    = re.compile("\s*(PUSH)\s+(\d+)\s*")
re_label   = re.compile("\s*([a-z0-9_]+:)\s*")
re_op      = re.compile("\s*([A-Z]+)\s*")
re_lop     = re.compile("\s*([A-Z]+)\s+([a-z0-9_]+)\s*")

class WhitespaceAssemblerParser(object):

    def __init__(self):
        super(WhitespaceAssemblerParser, self).__init__()

    def parse(self, text):
        result = []
        for index, line in enumerate(text.splitlines()):
            if line.strip() == "":
                continue
            for regex in [re_comment, re_push, re_label, re_lop, re_op]:
                match = regex.match(line)
                if match:
                    result.append(match.groups())
                    break
            else:
                raise ValueError("Parse error at line %d: unknown line [%r]" % (index, line))
        return result

class WhitespaceAssembler(object):

    TOKENS_1OP = ["dup", "swap", "pop", "add", "sub", "mul", "div", "mod", "get", "set", "ret", "halt", "write", "out", "read", "in"]
    TOKENS_2OP = ["call", "jump", "jumpz", "jumpn"]

    def __init__(self):
        super(WhitespaceAssembler, self).__init__()
        self.buf = StringIO()

    def assemble(self, tokens):
        for token in tokens:
            name = token[0].lower()
            if name in self.TOKENS_1OP:
                if hasattr(self, name):
                    getattr(self, name)()
                else:
                    raise ValueError("Unknown operation %s!" % name)
            elif name in self.TOKENS_2OP:
                if hasattr(self, name):
                    getattr(self, name)(tokens[1])
                else:
                    raise ValueError("Unknown operation %s %s!" % (name, tokens[1]))
            elif name == "push":
                self.push(int(token[1]))
            elif name[-1] == ":":
                self.label(name[:-1])
            else:
                raise ValueError("Unknown operation %s!" % name)

    # Stack manipulation
    def push(self, x):
        buf = self.buf
        # push number
        buf.write("  ")
        # positive sign
        buf.write(" ")
        for c in bin(x)[2:].zfill(8).lstrip("0"):
            if c == "0":
                # zero
                buf.write(" ")
            else:
                # one
                buf.write("\t")
        # end parameter
        buf.write("\n")

    def dup(self):
        self.buf.write(" \n ")

    def swap(self):
        self.buf.write(" \n\t")

    def pop(self):
        self.buf.write(" \n\n")

    # Arithmetic
    def add(self):
        self.buf.write("\t   ")

    def sub(self):
        self.buf.write("\t  \t")

    def mul(self):
        self.buf.write("\t  \n")

    def div(self):
        self.buf.write("\t \t ")

    def mod(self):
        self.buf.write("\t \t\t")

    # Heap
    def set(self):
        self.buf.write("\t\t ")

    def get(self):
        self.buf.write("\t\t\t")

    # Flow control

    def call(self, label):
        self.buf.write("\n \t%s\n" % label)

    def jump(self, label):
        self.buf.write("\n \n%s\n" % label)

    def jumpz(self, label):
        self.buf.write("\n\t %s\n" % label)

    def jumpn(self, label):
        self.buf.write("\n\t\t%s\n" % label)

    def ret(self):
        self.buf.write("\n\t\n")

    def halt(self):
        self.buf.write("\n\n\n")

    # io
    def write(self):
        # print top of stack
        self.buf.write("\t\n  ")

if __name__ == "__main__":
    import sys
    from pprint import pprint
    wap = WhitespaceAssemblerParser()
    tokens = wap.parse(sys.stdin.read())
    wa = WhitespaceAssembler()
    pprint(wa.assemble(tokens))
