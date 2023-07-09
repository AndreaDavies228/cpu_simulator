from import_file import instruction_list
from memory import *

class CPU:
  def __init__(self) -> None:
    self.number_registers = [0, 0, 0, 0, 0, 0, 0, 0]
    self.PC = 0
    self.instruction_dict = {}
    for i in instruction_list:
      self.instruction_dict[self.PC] = i
      self.PC += 4
    self.PC = 0
    self.user_display = ''
    self.cache_memory = Cache()
    self.cache_status = 1
    self.main_memory = MainMemory()

  def update_display(self, to_update):
    self.user_display = to_update
    print(self.user_display)

  def store_value_to_register(self, value_to_store, register_address):
    index = int(register_address, 2)
    self.number_registers[index] = bin(value_to_store)[2:]
    self.update_display(f"{(value_to_store)} was stored to register {index}")

  def load_value_from_register(self, register_address):
    index = int(register_address, 2)
    int_value = int(str(self.number_registers[index]), 2)
    return int_value

  def add(self, instruction):
    source_one = instruction[6:11]
    source_two = instruction[11:16]
    store = instruction[16:21]
    num1 = self.load_value_from_register(source_one)
    num2 = self.load_value_from_register(source_two)
    self.update_display(f"Performing addition of {num1} and {num2}.")
    calculated_value = num1 + num2
    self.update_display(f"Result is {calculated_value}.")
    self.store_value_to_register(calculated_value, store)
    self.PC += 4
    return

  def addi(self, instruction):
    source_one = instruction[6:11]
    store = instruction[11:16]
    imm = instruction[16:]
    num1 = self.load_value_from_register(source_one)
    num2 = int(imm, 2)
    self.update_display(f"Performing addition of {num1} and {num2}.")
    calculated_value = num1 + num2
    self.update_display(f"Result is {calculated_value}.")
    self.store_value_to_register(calculated_value, store)
    self.PC += 4
    return

  def sub(self, instruction):
    source_one = instruction[6:11]
    source_two = instruction[11:16]
    store = instruction[16:21]
    num1 = self.load_value_from_register(source_one)
    num2 = self.load_value_from_register(source_two)
    self.update_display(f"Performing subtraction of {num2} from {num1}.")
    calculated_value = num1 - num2
    self.update_display(f"Result is {calculated_value}")
    self.store_value_to_register(calculated_value, store)
    self.PC += 4
    return
  
  def slt(self, instruction):
    source_one = instruction[6:11]
    source_two = instruction[11:16]
    store = instruction[16:21]
    num1 = self.load_value_from_register(source_one)
    num2 = self.load_value_from_register(source_two)
    self.update_display(f"Performing comparison of {num1} and {num2}.")
    if num1 < num2:
      result = 1
      self.update_display(f"{num2} is greater than {num1}.")
    else:
      result = 0
      self.update_display(f"{num1} is greater or equal to {num2}.")
    self.store_value_to_register(result, store)
    self.PC += 4
    return
  
  def bne(self, instruction):
    source_one = instruction[6:11]
    source_two = instruction[11:16]
    offset = instruction[16:]
    num1 = self.load_value_from_register(source_one)
    num2 = self.load_value_from_register(source_two)
    self.update_display(f"Performing comparison of {num1} and {num2}.")
    if num1 != num2:
      self.PC = (self.PC + 4) + int(offset, 2) * 4
      self.update_display(f"Values don't match. Branching to instruction {self.PC}.")
    else:
      self.PC += 4
      self.update_display(f"Values match. Progressing to instruction {self.PC}.")
    return self.PC
  
  def j(self, instruction):
    target = int(instruction[6:], 2)
    self.update_display(f"Jumping to instruction {target * 4}.")
    return target * 4

  def jal(self, instruction):
    target = int(instruction[6:], 2)
    self.update_display(f"Saving link to {self.PC + 4}.")
    self.store_value_to_register(self.PC + 4, "111")
    self.update_display(f"Jumping to instruction {target * 4}.")
    return target * 4
  
  def lw(self, instruction):
    source_one = instruction[6:11]
    store = instruction[11:16]
    offset = instruction[16:]
    position = int(source_one, 2) + int(offset, 2)
    result = self.load_from_memory(position)
    self.update_display(f"Loaded {result} from memory position {position}.")
    result = int(result)
    self.store_value_to_register(result, store)
    self.PC += 4
    return
  
  def load_from_memory(self, address):
    if self.cache_status == 1:
      result = self.cache_memory.read(address)
      if result != False:
        return result
      else:
        data = self.main_memory.read(address)
        self.cache_memory.replace_entry(address, data)
        #self.update_display(f"Replaced {data} from memory position {address} in cache.")
        return data

    if self.cache_status == 0:
      return self.main_memory.read(address)

  
  def sw(self, instruction):
    store = instruction[6:11]
    source_one = instruction[11:16]
    offset = instruction[16:]
    result = self.load_value_from_register(source_one)
    position = int(store, 2) + int(offset, 2)
    self.save_to_memory(result, position)

    

    self.update_display(f"Saved {result} from register {int(source_one, 2)} to memory position {position}.")
    self.PC += 4
    return

  def save_to_memory(self, data, address):
    if self.cache_status == 1:
      self.cache_memory.write(address, data)
      self.main_memory.write(address, data)
    if self.cache_status == 0:
      self.main_memory.write(address, data)


  def cache_operation(self, instruction):
    code = instruction[11:16]
    if code == "00000":
      self.update_display(f"Turning cache off.")
      self.set_memory("off")
      #cache off
    if code == "00001":
      self.update_display(f"Turning cache on.")
      self.set_memory("on")
      #cache on
    if code == "00010":
      self.update_display(f"Flushing cache.")
      self.flush_cache()
      #flush cache
    self.PC += 4
    return
  
  def set_memory(self, memory):
    if memory == "off":
      self.cache_status = 0
    if memory == "on":
      self.cache_status = 1
  
  def flush_cache(self):
    self.cache_memory.flush_cache()

  
  def halt(self):
    self.update_display(f"Terminating execution.")
    exit()



      

  def binary_reader(self):    
    instruction = self.instruction_dict[self.PC]
    if len(instruction) != 32:
      self.update_display("Invalid Instruction Length")
      return
    opcode = instruction[:6]
    if opcode == "000000":
        function_code = instruction[26:]
        if function_code == "100000":
          self.add(instruction)
        if function_code == "100010":
          self.sub(instruction)
        if function_code == "101010":
          self.slt(instruction)
    if opcode == "001000":        
      self.addi(instruction)
    if opcode == "000101":
      self.PC = self.bne(instruction)
    if opcode == "000010":
      self.PC = self.j(instruction)
    if opcode == "000011":
      self.PC = self.jal(instruction)
    if opcode == "100011":
      self.lw(instruction)
    if opcode == "101011":
      self.sw(instruction)
    if opcode == "101111":
      self.cache_operation(instruction)
    if opcode == "111111":
      self.halt()

  def process_instructions(self):
    if self.instruction_dict == {}:
      print("No instructions in list.")
      exit()
    while self.PC <= max(k for k, v in self.instruction_dict.items()):
      self.update_display(f"\nProcessing instruction {self.PC}...")
      self.binary_reader()





cpu = CPU()

cpu.process_instructions()