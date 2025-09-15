import unittest

class MyObj():
  def __init__(self,name,value):
    self.name = name
    self.value = value


object_list = [
  MyObj('obj1', 10),
  MyObj('obj2', 20),
  MyObj('obj3', 30)
]

found = next((v for v in object_list if v.name == 'obj1'), False)

if found:
  print('found', found)
else:
  print('not found', found)


