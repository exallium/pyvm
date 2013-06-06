#!/usr/bin/python2
#
#   VM.PY
#   This is the Virtual Machine itself.
#   Quite Simply, it consists of memory, and a CPU.
#   The loader lives in a different module, loader.py
from instructions import instruction_set, registers
from loader import loader
import operator

class Processor:
    def __init__(self, filename):
        self.memory = loader(filename)
        self.instruction_set = {v['opcode']: k 
                for k,v in instruction_set.iteritems()}
        self.registers = {v: k.lower() for k, v in registers.iteritems()}
        [setattr(self, k, 0) for k in self.registers.values()]

        while (self.do_instruction()):
            pass

        from pprint import pprint
        pprint({reg: getattr(self, reg) for reg in self.registers.values()})

    def do_instruction(self):
        """ Performs a single instruction """
        instruction = self.memory.get(self.ip, None)
        if not instruction:
            return False

        instruction = self.instruction_set.get(instruction)

        nbytes = instruction_set[instruction]['nbytes']

        operation = getattr(self, "op_%s" % instruction.lower())
        self.ip = operation(nbytes) or self.ip + nbytes

        return True

    def get_ops(self, nbytes):
        return [self.memory[self.ip + i] for i in xrange(1, nbytes)]

    def do_operation(self, nbytes, operation):
        ops = self.get_ops(nbytes)
        
        r0 = self.registers[ops[0]]
        r1 = self.registers[ops[1]]

        setattr(self, r0, operation(getattr(self, r0), getattr(self, r1)))

    def op_add(self, nbytes):
        self.do_operation(nbytes, operator.add)

    def op_sub(self, nbytes):
        self.do_operation(nbytes, operator.sub)

    def op_and(self, nbytes):
        self.do_operation(nbytes, operator.and_)

    def op_or(self, nbytes):
        self.do_operation(nbytes, operator.or_)

    def op_xor(self, nbytes):
        self.do_operation(nbytes, operator.xor)

    def op_shl(self, nbytes):
        self.do_operation(nbytes, operator.lshift)

    def op_shr(self, nbytes):
        self.do_operation(nbytes, operator.rshift)

    def op_mov(self, nbytes):
        ops = self.get_ops(nbytes)

        r0 = self.registers[ops[0]]
        r1 = self.registers[ops[1]]

        setattr(self, r0, getattr(self, r1))

    def op_ldm(self, nbytes):
        pass

    def op_ldi(self, nbytes):
        ops = self.get_ops(nbytes)
        r = self.registers[ops[0]]
        setattr(self, r, ops[1])

    def op_str(self, nbytes):
        pass

    def op_push(self, nbytes):
        pass

    def op_pop(self, nbytes):
        pass

    def op_inc(self, nbytes):
        pass

    def op_dec(self, nbytes):
        pass

    def op_bra(self, nbytes):
        new_ip = [hex(v) for v in self.get_ops(nbytes)]
        new_ip = ''.join(new_ip).replace('0x', '')
        return int(new_ip)

    def op_bne(self, nbytes):
        pass

    def op_beq(self, nbytes):
        pass

    def op_blt(self, nbytes):
        pass

    def op_ble(self, nbytes):
        pass

    def op_bgt(self, nbytes):
        pass

    def op_bge(self, nbytes):
        pass


Processor('out')
