import re

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

if __name__ == "__main__":
    import sys
    wap = WhitespaceAssemblerParser()
    res = wap.parse(sys.stdin.read())
    from pprint import pprint
    pprint(res)
