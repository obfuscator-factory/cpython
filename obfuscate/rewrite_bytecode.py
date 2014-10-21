import opcode
import opcodeorig
import marshal
import re
import inspect
import sys
import random
import dis
import most_used_opcodes


class RewriteBytecode:
    def __init__(self,seqs):
        self.seqs = seqs
    
    def rewrite_bytecode(self, code):


        i = 0
        opcodes = []
        index = []
        labels = dis.findlabels(code)
        n = 0
        code_havearg = 159
        code_noarg = 43
        seq_codes = []
        for seq in self.seqs:
            if seq[0] >= opcode.HAVE_ARGUMENT:
                code_havearg += 1
                seq_codes.append(code_havearg)
            else:
                code_noarg += 1
                seq_codes.append(code_noarg)
        while i < len(code):
            opcodes.append(opcode.opmap[opcodeorig.opname[ord(code[i])]])
            
            index.append(i)
            for n, seq in enumerate(self.seqs):
                if i >= len(seq) and opcodes[-len(seq):] == seq:
                    #check if there is no jump to one of the opcodes in the sequence
                    if [j for j in range(1, len(seq) + 1) if index[-j] in labels]: 
                        continue
                    newcode = code[:index[-len(seq)]]
                    if seq[0] >= opcode.HAVE_ARGUMENT:
                        newcode += chr(seq_codes[n]) + code[index[-len(seq)]+1:index[-len(seq)]+3] # 2 bytes of args
                    else:
                        newcode += chr(seq_codes[n])
                    for j, op in enumerate(seq[1:]):
                        if op >= opcode.HAVE_ARGUMENT:
                            newcode += chr(random.randint(opcode.HAVE_ARGUMENT, 254)) + \
                                    code[index[-len(seq)+j+1]+1:index[-len(seq)+j+1]+3] # 2 bytes of args
                            
                        else:
                            newcode += chr(random.randint(1, opcode.HAVE_ARGUMENT-1))
                    opcodes[-1] = -1
                    if seq[-1] >= opcode.HAVE_ARGUMENT:
                        code = newcode + code[index[-1]+3:]
                    else:
                        code = newcode + code[index[-1]+1:]
                        
            
            if ord(code[i]) >= opcode.HAVE_ARGUMENT:
                i += 2
            i += 1

            
        return code

    
        
    def rewrite_co(self, co):
        return type(self.rewrite_co.__code__)(co.co_argcount, 
                co.co_nlocals, 
                co.co_stacksize, 
                co.co_flags, 
                self.rewrite_bytecode(co.co_code), 
                tuple((self.rewrite_co(const) if inspect.iscode(const) else const for const in co.co_consts)), 
                co.co_names, 
                co.co_varnames, 
                co.co_filename, 
                co.co_name, 
                co.co_firstlineno, 
                co.co_lnotab, 
                co.co_freevars, 
                co.co_cellvars)



if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage :"+sys.argv[0] + " <in.pyc> <out.pyc> <opcodes sequences file>" )
        exit()
    inp = sys.argv[1]
    fi = open(inp, 'rb')
    code = fi.read()
    fi.close()
    o = marshal.loads(code[8:])
    opcodes = most_used_opcodes.MostUsedOpcodes(sys.argv[3])
    r = RewriteBytecode(opcodes.seqs)
    newo = r.rewrite_co(o)
    out = open(sys.argv[2],'wb')
    out.write(code[:8])
    marshal.dump(newo, out)
    print "generated", sys.argv[2]
