from compiler_functions import *

""" Instruction 	Operands	        Meaning
    add 	        Rs, Rt, Rd 	        Rd <- Rs + Rt;
    addi 	        Rs, Rd, immd 	    Rt <- Rs + immd
    sub 	        Rs, Rt, Rd 	        Rd <- Rs - Rt
    slt 	        Rs, Rt, Rd 	        If (Rs < Rt) then Rd <- 1 else Rd <- 0
    bne 	        Rs, Rt, offset 	    If (Rs not equal Rt) then PC <- (PC + 4) + offset * 4
    j	            target 	            PC <- target * 4
    jal 	        target 	            R7 <- PC + 4; PC <- target *4
    lw 	            Rs, Rt, offset 	    Rt <- MEM[Rs + offset]
    sw 	            Rs, Rt, offset 	    MEM[Rs + offset] <- Rt
    cache 	        Code 	            Code = 0(Cache off) Code = 1(Cache on), Code = 2(Flush cache)
    halt 	        ; 	                Terminate Execution 
    
 
    """

my_file = open("input.txt", "r")
  
data = my_file.read()
instructions = data.split("\n")
my_file.close()

list = [i.split() for i in instructions]

instruction_list = []

for i in list:
     if i[0].lower() == "add":
        binary = add(int(i[1]),int(i[2]),int(i[3]))
        instruction_list.append(binary)
     if i[0].lower() == "addi":
        binary = addi(int(i[1]),int(i[2]),int(i[3]))
        instruction_list.append(binary)
     if i[0].lower() == "sub":
        binary = sub(int(i[1]),int(i[2]),int(i[3]))
        instruction_list.append(binary)
     if i[0].lower() == "slt":
        binary = slt(int(i[1]),int(i[2]),int(i[3]))
        instruction_list.append(binary)
     if i[0].lower() == "bne":
        binary = bne(int(i[1]),int(i[2]),int(i[3]))
        instruction_list.append(binary)
     if i[0].lower() == "j":
        binary = j(int(i[1]))
        instruction_list.append(binary)
     if i[0].lower() == "jal":
        binary = jal(int(i[1]),int(i[2]),int(i[3]))
        instruction_list.append(binary)
     if i[0].lower() == "lw":
        binary = lw(int(i[1]),int(i[2]),int(i[3]))
        instruction_list.append(binary)
     if i[0].lower() == "sw":
        binary = sw(int(i[1]),int(i[2]),int(i[3]))
        instruction_list.append(binary)
     if i[0].lower() == "cache":
        binary = cache(int(i[1]))
        instruction_list.append(binary)
     if i[0].lower() == "halt":
        binary = halt()
        instruction_list.append(binary)                                           
    