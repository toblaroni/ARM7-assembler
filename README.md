# ARMv4T-Assembler
The outcome of this project is for the assembler to be able to accept a subset of ARM assembly and output binary that is executable by an ARM7 processor.

### What is ARM7?
ARM (Advanced RISC Machines) is a "family of RISC instruction set architectures". ARM creates the instruction sets which are then licensed to other companies that make the processors. The most popular ARM7 *cores* were the ARM7TDMI and ARM7TDMI-S. 

#### ARM7 vs ARMv7
Here's why you should do your research before you start programming - lesson learnt (i hope)...

ARM7 != ARMv7. ARM7 is a set of **cores**. ARMv7 is an **ISA**. That is so stupid. WHy would they name it like that...

This is all starting to make more sense. Okay. I was trying to implement ARMv7 ISA while looking at ARM7 assembly examples. Riiiight....

### Architecture vs Core?
The *architecture* is the specification that defines how the processor should work. It defines things like:
- Instruction set
- Register Layout
- Memory Model
- Operation modes

The cortex is the *actual CPU implementation design*. Different cores can run the same architecture but have different performance, power consumption, clock speeds, etc. 
