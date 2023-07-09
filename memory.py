class MainMemory():
  def __init__(self):
    self.data = ["0"] * 32


  def read(self, address):
    data = self.data[address]
    print("Reading memory...")
    return data
  

  def write(self, address, data):
    self.data[address] = data
    print("Writing to memory...")

  
class Cache():
  def __init__(self):

    self.data = [
      {"tag": None, "data": ""}, 
      {"tag": None, "data": ""}, 
      {"tag": None, "data": ""}, 
      {"tag": None, "data": ""}
      ]
    self.fifo_index = 0

  def write(self, address, data):
    
    entry = self.get_entry(address)
    if entry is not None:
      print("Overwriting cache...")
      entry["data"] = data
    else:
      print("Writing to cache...")
      self.replace_entry(address, data)


  def read(self, address):
    print("Reading from cache...")
    data = None
    entry = self.get_entry(address)
    if entry is not None:
      print("Read from cache")
      data = entry["data"]
      return data
    else:
      print("Read from memory")
      return False
    


  def get_entry(self, address):
    for entry in self.data:
      if entry["tag"] == address:
          print(f"In cache. ", end="")
          return entry

    print(f"No entry in cache. ", end="")
    return None

  def replace_entry(self, address, data):
    index = self.fifo_policy()
    self.data[index] = {"tag": address, "data": data}

  def fifo_policy(self):
    index = self.fifo_index
    self.fifo_index += 1
    if self.fifo_index == len(self.data):
      self.fifo_index = 0

    return index
  
  def flush_cache(self):
    self.data = [
      {"tag": None, "data": ""}, 
      {"tag": None, "data": ""}, 
      {"tag": None, "data": ""}, 
      {"tag": None, "data": ""}
      ]
    