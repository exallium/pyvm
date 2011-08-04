#!/usr/bin/python2
#
#   LOADER.PY
#   Takes a file, loads it into a dict, and hands it back
def loader(infile):
    fin = open(infile, 'rb')
    sin = fin.read().split('\n')
    for (index, op) in enumerate(sin):
        sin[index] = [item for item in op.split(' ') if item]
    sin = [item for item in sin if item]
    memory = {}
    for item in sin:
        ptr = int(item[0])          # 'Where'
        for op in item[1:]:
            memory[ptr] = int(op)   # 'What'
            ptr += 1                # 'Where now?'

    # Note, order does not matter =)
    return memory
