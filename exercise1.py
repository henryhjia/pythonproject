#!/usr/bin/python3
# Henry Jia 2019
import datetime

class Exercise1:
  """
  """
  def checkSomething(self, a:int, b:int) -> None:
    """
    """
    print ("\n*********** function checkSomthing():")

    for i in range(0,5):
      print(i)

    s1 = "{} is divisible by {}"
    s2 = "{} is not divisible to {}"

    if a% b == 0:
        print(s1.format(a,b))
    else:
        print(s2.format(a,b))

  def mystring(self) -> None:
    """
    """
    print ("\n*********** function mystring():")

    c = "This is Henry"
    print (c)
    print (c + ' and Jean')
    print ("max=", max(c))
    print ("find Henry")
    print (c.find('Henry'))

    L = [1, "a", "string", 1+2]
    print (L)
    L.append(6)
    print (L)
    L.pop()
    print (L)
    print (L[1])

    tup = (1, "b", "henry", 2+4)
    print (tup)
    print (tup[0])
   
    i=1
    while (i<=10):
      print (i)
      i+=1

    print ("")

    s1 = "hello world"
    for i1 in s1:
	    print(i1)

  def mylist(self) -> None:
    """
    """
    myl = [7,2,10,4,5,6]
    print ("\n*********** function mylist():")
    print (myl)
    print ('reverse list with slicing:  ', myl[::-1])
    myl.reverse()
    print ('reverse list with reverse():', myl)
    myl.sort()
    print (myl)
    print ("max =", max(myl))
    print ("min =", min(myl))

    l1 = [['henry',10], ['Jean', 20]]
    print (l1)

  def myinput(self) -> None:
    """
    """
    print ("\n*********** function myinput():")
    year = input("Please enter your birth year: [default: 1960]")

    if len(year) !=4 or not year.isdigit():
        print ("Sorry, wrong format, set default to 1960")
        year = 1960
    else:
        print ("year=", year)

    return 1,2,year

  def test_args(self, one:str, two:str, **args) -> None:
    """
    """
    print ("\n*********** funtion test_args():")
    print (one)
    print (args)

  def print_number(self, n:int) -> None:
    print ("\n*********** recursion function print_number(n):")
    print (n)
    n -= 1
    if n:
      self.print_number(n)
    print (n)

  def mydictionary(self) -> None:
    """
    """
    print ("\n*********** function mydictionary():")
    dic = {'Jie':1964, 'Hong': 1960}
    print ('dictionary:', dic)
    print ('value of the key Jie:', dic['Jie'])
    print ('value of the key Hong:', dic['Hong'])

    mykeys = dic.keys()
    myvalues = dic.values()
    print ('keys:', mykeys)
    print ('values:', myvalues)

def main():

  exec = Exercise1()

  exec.checkSomething(4,2)
  exec.mystring()
  exec.mylist()
  t1, t2, year = exec.myinput()
  print ("t1=", t1)
  print ("t2=", t2)
  print ("year=", year)

  exec.test_args(one="henry", two="jia", three="how are you")

  mydate = datetime.datetime.now()
  print ('mydate datetime.now=', mydate)

  exec.print_number(10)

  exec.mydictionary()

if __name__ == "__main__":
    main()
