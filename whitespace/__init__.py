import re
from StringIO import StringIO

re_comment = re.compile("\s*;.*")
re_push    = re.compile("\s*(push)\s+(\d+)\s*")
re_label   = re.compile("\s*([a-z0-9_]+:)\s*")
re_op      = re.compile("\s*([A-Za-z]+)\s*")
re_lop     = re.compile("\s*([A-Za-z]+)\s+([a-z0-9_]+)\s*")

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
                if match and regex == re_comment:
                    break
                elif match:
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
        self.reset()

    def reset(self):
        self.labels = dict()
        self.buf = StringIO()

    def get_result(self):
        return self.buf.getvalue()

    def labelref(self, name):
        if not name in self.labels:
            label = bin(len(self.labels))[2:].replace("1", "\t").replace("0", " ")
            self.labels[name] = label
        return self.labels[name]

    def assemble(self, tokens):
        for token in tokens:
            name = token[0].lower()
            if len(token) > 1:
                labelname = token[1].lower()
            elif name[-1] == ":":
                labelname = name[:-1]
            else:
                labelname = None
            if name in self.TOKENS_1OP:
                if hasattr(self, name):
                    getattr(self, name)()
                else:
                    raise ValueError("Unknown operation %s!" % name)
            elif name in self.TOKENS_2OP:
                if hasattr(self, name):
                    getattr(self, name)(labelname)
                else:
                    raise ValueError("Unknown operation %s %s!" % (name, tokens[1]))
            elif name == "push":
                self.push(int(token[1]))
            elif name[-1] == ":":
                self.label(labelname)
            else:
                raise ValueError("Unknown operation %s!" % name)

    # Stack manipulation
    def push(self, x):
        buf = self.buf
        # push number
        buf.write("  ")
        if x > 0:
            # positive sign
            buf.write(" ")
        else:
            # negative sign
            buf.write("\t")
        for c in bin(abs(x))[2:].lstrip("0"):
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
    def label(self, label):
        self.buf.write("\n  %s\n" % self.labelref(label))

    def call(self, label):
        self.buf.write("\n \t%s\n" % self.labelref(label))

    def jump(self, label):
        self.buf.write("\n \n%s\n" % self.labelref(label))

    def jumpz(self, label):
        self.buf.write("\n\t %s\n" % self.labelref(label))

    def jumpn(self, label):
        self.buf.write("\n\t\t%s\n" % self.labelref(label))

    def ret(self):
        self.buf.write("\n\t\n")

    def halt(self):
        self.buf.write("\n\n\n")

    # input/output
    def write(self):
        # print top of stack as char
        self.buf.write("\t\n  ")

    def output(self):
        # print top of stack as number
        self.buf.write("\t\n \t")

    def read(self):
        # read to the top of stack pointer as char
        self.buf.write("\t\n\t ")

    def input(self):
        # read to the top of stack pointer as number
        self.buf.write("\t\n\t\t")

if __name__ == "__main__":
    import sys
    from pprint import pprint
    wap = WhitespaceAssemblerParser()
    tokens = wap.parse(sys.stdin.read())
    wa = WhitespaceAssembler()
    pprint(wa.assemble(tokens))
