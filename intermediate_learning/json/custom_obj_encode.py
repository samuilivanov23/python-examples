import json

class User:
  def __init__(self, name, age, active, balance, friends):
    self.name = name
    self.age = age
    self.active = active
    self.balance = balance
    self.friends = friends

class Player:
  def __init__(self, name, nickname, level):
    self.name = name
    self.nickname = nickname
    self.level = level

def encode_obj(obj):
  ### Takes custom objects and returns dict representation of it
  ### as well as module and class names.

  # Populate the result dict with the additional class and module fields
  obj_dict = {
    "__class__": obj.__class__.__name__,
    "__module__": obj.__module__
  }

  # Populate the result dict with the actual object properties 
  obj_dict.update(obj.__dict__)

  return obj_dict

def decode_dict(dict):
  if "__class__" in dict:
    class_name = dict.pop("__class__")
    module_name = dict.pop("__module__")
    module = __import__(module_name)
    class_ = getattr(module, class_name)
    obj = class_(**dict)
  else:
    obj = dict
  
  return obj

user = User(name = "John",age = 28, friends = ["Jane", "Tom"], balance = 20.70, active = True)
userJSON = json.dumps(user,default=encode_obj,indent=4, sort_keys=True)
print(userJSON)

user_decoded = json.loads(userJSON, object_hook=decode_dict)
print(type(user_decoded))


player = Player('Max', 'max1234', 5)
playerJSON = json.dumps(player,default=encode_obj,indent=4, sort_keys=True)
print(playerJSON)

player_decoded = json.loads(playerJSON, object_hook=decode_dict)
print(type(player_decoded))
