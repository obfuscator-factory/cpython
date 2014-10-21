from random import shuffle

normal_opcodes = {'s0': 0, 's1': 1, 's2': 2, 's3': 3, 's4': 4, 's5': 5,
                  's9': 9, 's10': 10, 's11': 11, 's12': 12, 's13': 13,
                  's15': 15, 's19': 19, 's20': 20, 's21': 21, 's22': 22,
                  's23': 23, 's24': 24, 's25': 25, 's26': 26, 's27': 27,
                  's28': 28, 's29': 29, 's54': 54, 's55': 55, 's56': 56,
                  's57': 57, 's58': 58, 's59': 59, 's60': 60, 's61': 61,
                  's62': 62, 's63': 63, 's64': 64, 's65': 65, 's66': 66,
                  's67': 67, 's68': 68, 's70': 70, 's71': 71, 's72': 72,
                  's73': 73, 's74': 74, 's75': 75, 's76': 76, 's77': 77,
                  's78': 78, 's79': 79, 's80': 80, 's81': 81, 's82': 82,
                  's83': 83, 's84': 84, 's85': 85, 's86': 86, 's87': 87,
                  's88': 88, 's89': 89
                  }


slice_opcodes = {'s30': 30, 's40': 40, 's50': 50, }


arg_opcodes = {'s90': 90, 's91': 91, 's92': 92, 's93': 93, 's94': 94,
               's95': 95, 's96': 96, 's97': 97, 's98': 98, 's99': 99,
               's100': 100, 's101': 101, 's102': 102, 's103': 103,
               's104': 104, 's105': 105, 's106': 106, 's107': 107,
               's108': 108, 's109': 109, 's110': 110, 's111': 111,
               's112': 112, 's113': 113, 's114': 114, 's115': 115,
               }
argn_opcodes = {'s116': 116, 's119': 119, 's120': 120, 's121': 121,
                's122': 122, 's124': 124, 's125': 125, 's126': 126,
                's130': 130, 's131': 131, 's132': 132, 's133': 133,
                's134': 134, 's135': 135, 's136': 136, 's137': 137,
                's143': 143,
                }


ext_opcodes = {'s145': 145, 's146': 146, 's147': 147 }



def genopcodes(in_header, in_python, h_out, py_out, doshuffle):

    with open(in_python, "r") as opcode_py_tpl:
       template_py = opcode_py_tpl.read()
    with open(in_header, "r") as opcode_h_tpl:
       template_h = opcode_h_tpl.read()


    def shuffle_opcodes(ops):
        keys = ops.keys()
        values = ops.values()
        shuffle(values)
        return dict(zip(keys, values))

    nshuffle_opcodes = lambda x: x
    if not doshuffle:
        shuffle_opcodes = nshuffle_opcodes

    p_normal_opcodes = shuffle_opcodes(normal_opcodes)
    p_slice_opcodes = shuffle_opcodes(slice_opcodes)
    p_arg_opcodes = nshuffle_opcodes(arg_opcodes)
    p_arg_opcodes.update(shuffle_opcodes(argn_opcodes))
    p_ext_opcodes = shuffle_opcodes(ext_opcodes)

    merged = {}
    merged.update(p_normal_opcodes)
    merged.update(p_slice_opcodes)
    merged.update(p_arg_opcodes)
    merged.update(p_ext_opcodes)
    merged['s_ward'] = min(p_arg_opcodes.values())
    merged_values = set(merged.values())

    def cond(n):
        return ((n & 3 == 1) and
                ((p_arg_opcodes['s131'] + n + 0) not in merged_values) and
                ((p_arg_opcodes['s131'] + n + 1) not in merged_values) and
                ((p_arg_opcodes['s131'] + n + 2) not in merged_values)
                )

    n = 1
    while not cond(n):
        n += 1
    merged['s140'] = p_arg_opcodes['s131'] + n
    merged['s141'] = p_arg_opcodes['s131'] + n + 1
    merged['s142'] = p_arg_opcodes['s131'] + n + 2

    with open(h_out, "w") as out_header:
        out_header.write(template_h.format(**merged))
    with open(py_out, "w") as out_python:
        out_python.write(template_py.format(**merged))
    print "generated", h_out, py_out

if __name__ == '__main__':
    import sys
    doshuffle = sys.argv[1] == '--shuffle'
    py_in, h_in, py_out, h_out = sys.argv[2:]
    genopcodes(h_in, py_in, h_out, py_out, doshuffle)
