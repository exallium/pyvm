import sys
from instructions import load_instr, reg_dict

def main():
    if len(sys.argv) != 3:
        print 'assembler.py: usage: python assembler.py infile outfile'
        return

    instr_dir = load_instr()
    reg_dir = reg_dict()

    fin = open(sys.argv[1], 'r')
    instr_strings = fin.read()
    fin.close()
    instr_strings = instr_strings.split('\n')
    
    # The last one is garbage and there's no point in processing it
    instr_strings = instr_strings[:len(instr_strings)-1]

    # We capitalize every instruction, and then split each list by ' '
    for (index, string) in enumerate(instr_strings):
        instr_strings[index] = string.upper().split(' ')

    # We don't check whether or not END exists here.  We find it on
    # the go. As soon as we do, we're done.
    ip = 0

    #First pass is where the magic happens
    #Conversions are made and assembler directives are handled

    # Second Pass
    fout = open(sys.argv[2], 'w')
    
    # In pythonic form, we choose better just to ask forgivness later
    try:
        ip = 0
        for string in instr_strings:
            prev_ip = ip
            if string[0] == 'END': break
            fout.write("%s %s " % (ip, instr_dir[string[0]]['opcode']))
            ip = ip + 1
            if len(string) - 1 != instr_dir[string[0]]['nops']:
                print ('2pass: e: irregular number of ops for %s'
                    % string)
                return
            for strr in string[1:]:
                try:
                    fout.write("%s " % reg_dir[strr])
                    ip = ip + 1
                except KeyError:
                    if strr[0] == '#':
                        ip += 1
                        fout.write('%s ' % strr[1:])
                    elif strr[0] == '$':
                        ip += 2
                        item = int(strr[1:], 16)
                        fout.write('%s %s' % (item >> 8, item & 0xFF))
                    else:
                        print ('2pass: e: invalid operand prefix: %s'
                                % strr[0])
                        return
            if ip - prev_ip != instr_dir[string[0]]['nbytes']:
                print "2pass: e: invalid byte count for %s" % strr[0]
            fout.write('\n')
            
    except KeyError:
        print 'second pass: error: %s: invalid.' % string[0]

    fout.close()

main()
