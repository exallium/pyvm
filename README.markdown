# PYVM -- Python Virtual Machine
Author: Alex Hart
Date: July, 2011

#The point
Of this sotware is to explore the capabilities of python's high level syntax to
see how it can handle a low level programming environment.

#The Specifications
There are four 8bit accumulators (call them AX, BX, CX, and DX) 
There are two 16 bit index registers (SI and DI)
There are three 16 bit segment registers (DS, CS, and SS)
There is an 8bit status register
 * Negative bit
 * Zero bit
 * Carry bit
There is a stack poiner and instruction pointer
There are 65536 memory locations

#The instruction set
This set is meant to try to be as minimal as possible without being
overbearing.  Therefore, the decision was made to keep all of the separate
branch statements, for instance.
Arithmetic
==========
```
ADD acc1 acc2 -- Performs acc1 = acc1 + acc2
SUB acc1 acc2 -- Performs acc1 = acc1 - acc2
```
Logic
==========
```
AND acc1 acc2 -- Performs acc1 = acc1 & acc2
OR  acc1 acc2 -- Performs acc1 = acc1 | acc2
XOR acc1 acc2 -- Performs acc1 = acc1 ^ acc2
SHL acc1 acc2 -- Performs acc1 = acc1 << acc2
SHR acc1 acc2 -- Performs acc1 = acc1 >> acc2
```
Memory and Movement
==========
```
MOV  acc1 acc2 -- Copies contents of acc1 to acc2
LDM  acc1 $mem -- Puts val ($location) into acc1
LDI  acc1 #val -- Puts val (#value) into acc1
STR  acc1 $mem -- Puts acc1 into mem ($location)
PUSH acc1      -- Pushes acc1 onto stack and decrements stack pointer
POP  acc1      -- Pops the top of stack into acc1 and increments stack pointer
INC  acc1      -- Increments acc1
DEC  acc1      -- Decremens acc1
```
Branching
==========
```
BRA  acc1      -- Branch always to location stored in acc1
BNE  acc1      -- Branch if zero bit clear to location stored in acc1
BEQ  acc1      -- Branch if zero bit set to location stored in acc1
BLT  acc1      -- Branch if zero bit clear and negative bit set to location
BLE  acc1      -- Branch if zero bit set or negative bit set to location
BGT  acc1      -- Branch if zero bit clear and negative bit clear to location
BGE  acc1      -- Branch if zero bit set or negative bit clear to location
```

# The Assembler
Usage: python assembler.py infile outfile
outputs a vm runable script in the following format:
memorylocation opcode
Assembler Directives
==========
```
ORG $mem      -- Set the location to $mem
LABEL EQU val -- Set a constant val to LABEL
LABEL dw val  -- Declares a 16 bit word
LABEL db val  -- Declares an 8bit value
LABEL ds val  -- Declares a data segment
label:        -- Marks a location for later reference
END           -- EOF, required in every file
```
# Opcode
The opcode is split into sections depending on what type of instruction you are using. This makes it easier to quickly see what is going on.  This opcode is also joined with another 1 to 3 bytes of information.  These would be the operands.  
For example, add AX BX would compile to something like: 0x00 0x01 0xAB.  
Something more complex, like STR AX $C0DC would compile to something along the lines of 0x00 0x01 0xC0 0xDC

```
ADD  00000001
SUB  00000010

AND  00000100
OR   00000101
XOR  00000110
SHL  00010000
SHR  00010001

MOV  00001000
LDM  00001001 -- From Memory
LDI  00001010 -- Immediate
STR  00001011
PUSH 00001100
POP  00001101
INC  00001110
DEC  00001111

BRA  10000000
BNE  10010000
BEQ  10100000
BLT  10110000
BLE  11000000
BGT  11010000
BGE  11100000
```
