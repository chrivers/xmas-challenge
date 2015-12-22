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
                self.push(tokens[1])
            elif name[-1] == ":":
                self.label(name[:-1])
            else:
                raise ValueError("Unknown operation %s!" % name)

if __name__ == "__main__":
    import sys
    from pprint import pprint
    wap = WhitespaceAssemblerParser()
    tokens = wap.parse(sys.stdin.read())
    wa = WhitespaceAssembler()
    pprint(wa.assemble(tokens))
