from __future__ import print_function
import marshal
import inspect
import opcode
import sys
import most_used_opcodes

LENGTH_SEQ_MIN = 2
LENGTH_SEQ_MAX = 4
NUM_NEW_OPCODES = 6 # per sequence length


class VisitByteCode:
   
    def __init__(self):
        self.seqs = {i:{} for i in range(LENGTH_SEQ_MIN, LENGTH_SEQ_MAX+1)}

    def visit(self, bytecode):
        self.analyse(bytecode)
        for const in bytecode.co_consts:
            if inspect.iscode(const):
                self.visit(const)

    
    def read_bytecode(self, code):
        arg_left = 0
        for op in code.co_code:
            if arg_left > 0:
                arg_left -= 1
            else:
                yield(ord(op))
                if ord(op) >= opcode.HAVE_ARGUMENT:
                    arg_left = 2
                

    def analyse(self, code):
        key = ()
        for i, op in enumerate(self.read_bytecode(code)):
            key = key + (op,)
            for j in range(LENGTH_SEQ_MIN, min(i+LENGTH_SEQ_MIN, LENGTH_SEQ_MAX + 1)):
                self.seqs[j].setdefault(key[-j:], 0)
                self.seqs[j][key[-j:]] += 1




if __name__ == '__main__':
    
    if len(sys.argv) < 3:
        print("Usage: " + sys.argv[0] + " <out> <file1.pyc> <file2.pyc> <...>")
        exit()
    
    
    v = VisitByteCode()
    for i in range (2, len(sys.argv)):
        with open(sys.argv[i], "r") as fi:
            o = marshal.loads(fi.read()[8:])
        v.visit(o)

    sorted_seq = {}
    for k, seq in v.seqs.items():
        sorted_seq[k] = [s for s in sorted(seq.items(), key=lambda t: t[1],reverse=True)]
    
    muo = most_used_opcodes.MostUsedOpcodes(sys.argv[1])
    final_seqs = []
    for _, seqs in sorted_seq.items():
        for s in seqs[:NUM_NEW_OPCODES]:
            final_seqs += [s[0]]
    muo.seqs = final_seqs

