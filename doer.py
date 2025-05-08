from abc import ABC, abstractmethod

class Command(ABC):
  def __init__(self, prompt: str):
    self.prompt = prompt
  
  def execute(self) -> None:
    print(f"! executed: {self.prompt}")
  
class Doer:
  def __init__(self):
    self.commands = []
  
  def do(self, end_prompt: str = "-") -> None:
    prompt = ""
    
    while prompt != end_prompt:
      prompt = input("> ")
      
      command = Command(prompt)
      command.execute()
      
      self.commands.append(command)
      
    print("> does finished")
    return 