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
    
    instructions should be entered as functions, with the operands as arguments, followed by a comma (except for the final instruction):
    e.g.
    addi(1,2,3),
    add(2,3,4),
    halt()
    
    """

instruction_list = [


]
