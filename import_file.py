from compiler_functions import *

""" Instruction 	Operand arguments 	Meaning
    ADD 	        Rs, Rt, Rd 	        Rd <- Rs + Rt;
    ADDI 	        Rs, Rd, immd 	    Rt <- Rs + immd
    SUB 	        Rs, Rt, Rd 	        Rd <- Rs - Rt
    SLT 	        Rs, Rt, Rd 	        If (Rs < Rt) then Rd <- 1 else Rd <- 0
    BNE 	        Rs, Rt, offset 	    If (Rs not equal Rt) then PC <- (PC + 4) + offset * 4
    J 	            target 	            PC <- target * 4
    JAL 	        target 	            R7 <- PC + 4; PC <- target *4
    LW 	            Rs, Rt, offset 	    Rt <- MEM[Rs + offset]
    SW 	            Rs, Rt, offset 	    MEM[Rs + offset] <- Rt
    CACHE 	        Code 	            Code = 0(Cache off) Code = 1(Cache on), Code = 2(Flush cache)
    HALT 	        ; 	                Terminate Execution """

instruction_list = [


]
