# CPU Simulator

This is a simple CPU simulator, as a theoretical exrcise.
It will take a series of instruction functions, convert them to binary. Then process them in the CPU, saving to the cache or memory accordingly.
Explanaing of the processes will be output to the terminal as they are performed.

The following operations are supported:

|Instruction | Operand arguments | Meaning |
| ----------- | ----------- | ----------- |
|ADD | Rs, Rt, Rd | Rd <- Rs + Rt; |
|ADDI | Rs, Rd, immd | Rt <- Rs + immd |
|SUB | Rs, Rt, Rd | Rd <- Rs - Rt |
|SLT | Rs, Rt, Rd | If (Rs < Rt) then Rd <- 1 else Rd <- 0 |
|BNE | Rs, Rt, offset | If (Rs not equal Rt) then PC <- (PC + 4) + offset * 4 |
|J | target | PC <- target * 4 |
|JAL | target | R7 <- PC + 4; PC <- target *4 |
|LW | Rs, Rt, offset | Rt <- MEM[Rs + offset] |
|SW | Rs, Rt, offset | MEM[Rs + offset] <- Rt |
|CACHE | Code | Code = 0(Cache off) Code = 1(Cache on), Code = 2(Flush cache) |
|HALT |  | Terminate Execution  |

## Background

This simulator was created as my python programming project, as part of my Codecademy computer science course. 

## Sample Image

![Processing instructions](https://github.com/AndreaDavies228/cpu_simulator/blob/main/CPU_simulator.png)

## Instructions

The simulator is designed to run in Python 3.

First download the repository.
From the main directory, open input.txt in notepad.

```bash
$ notepad "input.txt"
```
Enter a list of instructions in the input file, refering to the table above
Each instruction should be one one line, starting with the instruction (e.g. ADD, ADDI), folowed by the operands in the order in the table, separated with whitespace.
The file currently contains the following instructions as an example:

>ADDI 1 2 3 <br>
>ADD 2 3 4 <br>
>HALT <br>

Then save the file.

Next run the file cpu.py in Python to execute the list of instructions.

```bash
$ python -m cpu
```

import_file.py processes the instructions in the text file using the functions in comiler_functions.py. The cache and memory are imported from the separate memory.py file. 

## Author

* Andrea Davies - Design and coding

## License

This project is licensed under the CC0 1.0 Universal Creative Commons License - see the LICENSE.md file for details.
