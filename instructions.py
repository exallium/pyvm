'''
This file allows for the loading of all the instructions into a hash map

filename: instructions.py
author: Alex Hart
Date: July, 2011
'''

def load_instr():
    '''
    This will load a dictionary of instructions into memory.
    nbytes is the total number of bytes that will end up in memory.
    '''
    return {
            'ADD':  {'opcode': 0x01, 'nops': 2, 'nbytes':3}, 
            'SUB':  {'opcode': 0x02, 'nops': 2, 'nbytes':3}, 
            'AND':  {'opcode': 0x04, 'nops': 2, 'nbytes':3}, 
            'OR':   {'opcode': 0x05, 'nops': 2, 'nbytes':3},
            'XOR':  {'opcode': 0x06, 'nops': 2, 'nbytes':3}, 
            'SHL':  {'opcode': 0x10, 'nops': 2, 'nbytes':3}, 
            'SHR':  {'opcode': 0x11, 'nops': 2, 'nbytes':3}, 
            'MOV':  {'opcode': 0x08, 'nops': 2, 'nbytes':3}, 
            'LDM':  {'opcode': 0x09, 'nops': 2, 'nbytes':4}, 
            'LDI':  {'opcode': 0x0A, 'nops': 2, 'nbytes':3},
            'STR':  {'opcode': 0x0B, 'nops': 2, 'nbytes':4}, 
            'PUSH': {'opcode': 0x0C, 'nops': 1, 'nbytes':2}, 
            'POP':  {'opcode': 0x0D, 'nops': 1, 'nbytes':2}, 
            'INC':  {'opcode': 0x0E, 'nops': 1, 'nbytes':2},
            'DEC':  {'opcode': 0x0F, 'nops': 1, 'nbytes':2}, 
            'BRA':  {'opcode': 0x80, 'nops': 1, 'nbytes':2}, 
            'BNE':  {'opcode': 0x90, 'nops': 1, 'nbytes':2}, 
            'BEQ':  {'opcode': 0xA0, 'nops': 1, 'nbytes':2},
            'BLT':  {'opcode': 0xB0, 'nops': 1, 'nbytes':2}, 
            'BLE':  {'opcode': 0xC0, 'nops': 1, 'nbytes':2}, 
            'BGT':  {'opcode': 0xD0, 'nops': 1, 'nbytes':2}, 
            'BGE':  {'opcode': 0xE0, 'nops': 1, 'nbytes':2},
            }

def reg_dict():
    return {
            'AX': 0x0A,
            'BX': 0x0B,
            'CX': 0x0C,
            'DX': 0x0D,
            'SI': 0x0E,
            'DI': 0x0F,
            'STATUS': 0x00,
            'IP': 0x01,
            'SP': 0x02,
            'DS': 0x03,
            'CS': 0x04,
            'SS': 0x05
            }
