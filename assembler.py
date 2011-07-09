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

    instr_strings = instr_strings[:len(instr_strings) - 1]
    
    # We capitalize every instruction, and then split each list by ' '
    for (index, string) in enumerate(instr_strings):
        if string.find(';') != -1:
            string = string[:string.find(';')]

        instr_strings[index] = [instr for instr in instr_strings[index] if instr != ';']
        instr_strings[index] = string.upper().split(' ')
        instr_strings[index] = [instr for instr in instr_strings[index] if instr != '']

    # We don't check whether or not END exists here.  We find it on
    # the go. As soon as we do, we're done.
    ip = 0

    # First thing we do is grab all of the labels.
    # We compile this list and spit them into their corresponding locations.
    # Label declarations are removed, label references are replaced with their
    # corresponding location
    labels = {}
    for string in instr_strings:
        for (index, item) in enumerate(string):
            if item[len(item) - 1] == ':':  # We have a label
                item = item.rstrip(':')
                if (item[0].isdigit() or instr_dir.get(item, None)
                        or reg_dir.get(item, None)):
                    print '1pass: e: ip=%s: %s is invalid label' % (ip, item)
                    return
                if labels.get(item, None):
                    print '1pass: e: ip=%s: %s is duplicate label' % (ip, item)
                    return
                labels[item] = ip
                string.remove('%s:' % item)
            elif labels.get(item, None):
                string[index] = '$%s' % labels.get(item)
            elif item[0] == '$':  # We have a memory address
                ip = ip + 2
            else:
                ip = ip + 1

    instr_strings = [string for string in instr_strings if string]

    # Now we can take care of directives
    ip = 0
    for string in instr_strings:
        for (index, item) in enumerate(string):
            if item == 'ORG' and item[index + 1][0] == '$':
                ip = int(item[index + 1][1:],16)
            #elif item == 'EQU':
            #   
            #elif item == 'DW':
            #elif item == 'DB':
            #elif item == 'DS':
    
    # Second Pass
    fout = open(sys.argv[2], 'w')
    
    # In pythonic form, we choose better just to ask forgivness later
    try:
        ip = 0
        for string in instr_strings:
            prev_ip = ip
            if string[0] == 'END': break
            if string[0] == 'ORG':
                if len(string) != 2:
                    print ('2pass: e: ip=%s: irregular number of ops for ORG' 
                            % ip)
                if string[1][0] == '$':
                    ip = int(string[1][1:], 16)
                    continue
                    
            fout.write("%s %s " % (ip, instr_dir[string[0]]['opcode']))
            ip = ip + 1
            if len(string) - 1 != instr_dir[string[0]]['nops']:
                print ('2pass: e: ip=%s: irregular number of ops for %s'
                    % (ip, string))
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
                        print ('2pass: e: ip=%s: invalid operand prefix: %s'
                                % (ip, strr[0]))
                        return
            if ip - prev_ip != instr_dir[string[0]]['nbytes']:
                print "2pass: e: ip=%s: invalid byte count for %s" % (ip,
                        strr[0])
            fout.write('\n')
            
    except KeyError:
        print 'second pass: error: ip=%s: %s: invalid.' % (ip, string[0])

    fout.close()

main()
