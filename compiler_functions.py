def add(rs, rt, rd):
    opcode = "000000"
    rs = bin(rs)[2:]
    while len(rs) < 5:
        rs = "0" + rs
    rt = bin(rt)[2:]
    while len(rt) < 5:
        rt = "0" + rt
    rd = bin(rd)[2:]
    while len(rd) < 5:
        rd = "0" + rd
    function = "100000"
    binary = opcode + rs + rt + rd + "00000" + function
    return binary

def addi(rs, rd, imm):
    opcode = "001000"
    rs = bin(int(rs))[2:]
    while len(rs) < 5:
        rs = "0" + rs    
    rd = bin(int(rd))[2:]
    while len(rd) < 5:
        rd = "0" + rd    
    imm = bin(int(imm))[2:]
    while len(imm) < 16:
        imm = "0" + imm    
    binary = opcode + rs + rd + imm
    return binary

def sub(rs, rt, rd):
    opcode = "000000"
    rs = bin(rs)[2:]
    while len(rs) < 5:
        rs = "0" + rs    
    rt = bin(rt)[2:]
    while len(rt) < 5:
        rt = "0" + rt    
    rd = bin(rd)[2:]
    while len(rd) < 5:
        rd = "0" + rd
    function = "100010"
    binary = opcode + rs + rt + rd + "00000" + function
    return binary

def slt(rs, rt, rd):
    opcode = "000000"
    rs = bin(rs)[2:]
    while len(rs) < 5:
        rs = "0" + rs    
    rt = bin(rt)[2:]
    while len(rt) < 5:
        rt = "0" + rt    
    rd = "00000"
    function = "101010"
    binary = opcode + rs + rt + rd + "00000" +  function
    return binary

def bne(rs, rt, offset):
    opcode = "000101"
    rs = bin(rs)[2:]
    while len(rs) < 5:
        rs = "0" + rs    
    rt = bin(rt)[2:]
    while len(rt) < 5:
        rt = "0" + rt    
    offset = bin(offset)[2:]
    while len(offset) < 16:
        offset = "0" + offset       
    binary = opcode + rs + rt + offset
    return binary

def j(target):
    opcode = "000010"
    target = bin(target)[2:]
    while len(target) < 26:
        target = "0" + target
    binary = opcode + target
    return binary

def jal(target):
    opcode = "000011"
    target = bin(target)[2:]
    while len(target) < 26:
        target = "0" + target
    binary = opcode + target
    return binary

def lw(rs, rt, offset):
    opcode = "100011"
    rs = bin(rs)[2:]
    while len(rs) < 5:
        rs = "0" + rs    
    rt = bin(rt)[2:]
    while len(rt) < 5:
        rt = "0" + rt    
    offset = bin(offset)[2:]
    while len(offset) < 16:
        offset = "0" + offset       
    binary = opcode + rs + rt + offset
    return binary

def sw(rs, rt, offset):
    opcode = "101011"
    rs = bin(rs)[2:]
    while len(rs) < 5:
        rs = "0" + rs    
    rt = bin(rt)[2:]
    while len(rt) < 5:
        rt = "0" + rt    
    offset = bin(offset)[2:]
    while len(offset) < 16:
        offset = "0" + offset    
    binary = opcode + rs + rt + offset
    return binary

def cache(code):
    opcode = "101111"
    base = "00000"
    code = bin(code)[2:]
    while len(code) < 5:
        code = "0" + code
    offset = "0000000000000000"   
    binary = opcode + base + code + offset
    return binary
      

def halt():
    opcode = "111111"
    binary = opcode + "00000000000000000000000000"
    return binary
