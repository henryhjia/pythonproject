#!/usr/bin/python3
# Henry Jia 2023
# Practice Object-oriented base class, subclass

class MyBase(object):
  """
  """
  def __init__(self, a:int=5, b:int=10, c="") -> None:
    """
    """
    self.a = a
    self.b = b
    self.c = c

  def __eq__(self, other: str) -> bool:
    """
    """
    if self.a == other.a and self.b == other.b and self.c == other.c:
      return True
    else:
      return False
  
  def __ne__(self, other: str) -> bool:
    """
    """
    if self.a != other.a or self.b != other.b or self.c != other.c:
      return True
    else:
      return False

  def __str__(self) -> str:
    """
    """
    return "c="+self.c+" a="+str(self.a)+" b="+str(self.b)

class MySubclass(MyBase):
  """
  """
  def __init__(self, a:int, b:int, c:str, mya:int, myb:int, myc:str) -> None:
    """
    """
    super(MySubclass, self).__init__(a=a,b=b,c=c)
    self.mya = mya
    self.myb = myb
    self.myc = myc
  
  def __str__(self) -> str:
    """
    """
    content = "a="+str(self.a)+" b="+str(self.b)+" c="+self.c + " mya="+str(self.mya) + " myb="+str(self.myb) + " myc="+self.myc
    return content

def main():
  print ("inheritance.py")

  new_item = MyBase(10,20,"Henry Jia")
  print (new_item)
  subitem = MySubclass(a=100,b=200,c="Claire", mya=1000,myb=2000,myc="Jean")
  print (subitem)

if __name__ == "__main__":
  main()