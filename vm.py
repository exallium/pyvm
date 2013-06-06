#!/usr/bin/python2
#
#   VM.PY
#   This is the Virtual Machine itself.
#   Quite Simply, it consists of memory, and a CPU.
#   The loader lives in a different module, loader.py
from instructions import instruction_set, registers
from loader import loader

class Processor:
    def __init__(self, filename):
        self.memory = loader(filename)
        self.instruction_set = {v['opcode']: k for k,v in instruction_set.iteritems()}

        [setattr(self, k.lower(), 0) for k in registers.keys()]

        while (self.do_instruction()):
            pass

    def do_instruction(self):
        """ Performs a single instruction """
        instruction = self.memory.get(self.ip, None)
        if not instruction:
            return False

        instruction = self.instruction_set.get(instruction)
        print instruction.lower()

        nops = instruction_set[instruction]['nops']
        nbytes = instruction_set[instruction]['nbytes']

        operation = getattr(self, "op_%s" % instruction.lower())
        self.ip = operation(nops, nbytes) or self.ip + nbytes

        return True

    def op_add(self, nops, nbytes):
        pass

    def op_sub(self, nops, nbytes):
        pass

    def op_and(self, nops, nbytes):
        pass

    def op_or(self, nops, nbytes):
        pass

    def op_xor(self, nops, nbytes):
        pass

    def op_shl(self, nops, nbytes):
        pass

    def op_shr(self, nops, nbytes):
        pass

    def op_mov(self, nops, nbytes):
        pass

    def op_ldm(self, nops, nbytes):
        pass

    def op_ldi(self, nops, nbytes):
        pass

    def op_str(self, nops, nbytes):
        pass

    def op_push(self, nops, nbytes):
        pass

    def op_pop(self, nops, nbytes):
        pass

    def op_inc(self, nops, nbytes):
        pass

    def op_dec(self, nops, nbytes):
        pass

    def op_bra(self, nops, nbytes):
        new_ip = [hex(self.memory[self.ip + i]) for i in xrange(1, nbytes)]
        new_ip = ''.join(new_ip).replace('0x', '')
        return int(new_ip)

    def op_bne(self, nops, nbytes):
        pass

    def op_beq(self, nops, nbytes):
        pass

    def op_blt(self, nops, nbytes):
        pass

    def op_ble(self, nops, nbytes):
        pass

    def op_bgt(self, nops, nbytes):
        pass

    def op_bge(self, nops, nbytes):
        pass


Processor('out')
