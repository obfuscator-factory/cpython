


import code as code_opcode
import opcode
import sys
import most_used_opcodes

def writec(inp, outp, opcodes, n_newop, start):
    new_opcode = "case " + str(n_newop) + ":\n" 

    for i,opcode in enumerate(opcodes):
        dest = start + ((i+1) % len(opcodes))
        if dest == start:
            dest = 0
        new_opcode += "dest = " + str(dest) + ";" +\
                code_opcode.code[opcode] + \
                "dest" + str(dest) + ": \n" 

    new_opcode = new_opcode[:-8]

    with open(inp, 'r') as inp:
        code = inp.read()

    switch = ""
    for i in xrange(1,len(opcodes)):
        switch += "case " + str(start + i) + ":\n" + \
                "\t goto dest" + str(start + i) + ";\n"



    code = code.replace('//##NEWOPCODES', 
            new_opcode + "\n//##NEWOPCODES")
    code = code.replace("//##GOTOSWITCH",
            switch + "\n//##GOTOSWITCH")
    with open(outp, 'w') as out:
        out.write(code)


if __name__ == "__main__":
    rewrite = sys.argv[1] == "--gen-opcodes"
    if rewrite:
        seqs = most_used_opcodes.MostUsedOpcodes(sys.argv[4]).seqs
        start_noarg = 43
        start_args = 159
        in_file = sys.argv[2]
        out_file =  sys.argv[3]
        for i, seq in enumerate(seqs):
            havearg =  seq[0] >= opcode.HAVE_ARGUMENT
            if havearg:
                start_args += 1
            else:
                start_noarg += 1
            #goto labels increase by 10 between each new opcodes
            #so one opcodes can only regroup a maximum sequence of 10 opcodes 
            writec(in_file, out_file, seq, start_args if havearg else start_noarg, i * 10)
            # next updates are made inplace
            in_file = out_file
    else:
        open(sys.argv[3],'w').write(open(sys.argv[2],'r').read())

