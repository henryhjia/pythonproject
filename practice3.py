#!/usr/bin/python3
# Henry Jia July 2023
import random
import math

class Exercise3(object):
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

  def test_print_pattern(self) -> int:
    print('************** test_print_pattern')  
    for i in range(5):
      for j in range(i):
        print(' ', end='')
      print('#')

    for i in range(5):
      for j in range(i):
        print('*', end='')
      print()  
    print()

    for count in range(5):
      print('*' * count)

    print()
    for count in range(5,0,-1):
      print('*' * count)

    print()
    print('jia', 'hong', sep='*')
    print('jia', 'hong', sep='$', end='#')
    print()

    amount = 1234567.12345
    print('$',format(amount,',.2f'), sep='', end='*')
    print()

    i = 0
    
    for i in range(10):
      # random.seed(10)
      ran1 = random.randint(1,100)
      ran2 = random.randrange(1,10)    
      ran3 = random.random()
      ran4 = random.uniform(1.0,10.0)
      print('i=', format(i,'d'), 'ran1=', format(ran1, '3d'), 'ran2=', 
            ran2, 'ran3=', format(ran3, '.2f'), 'ran4=', format(ran4, '.3f'))

    return ran1, ran2, ran3, ran4

  def file_read_write_exercise(self) -> None:
    ""
    print('************** file_read_write_exercise')  
    try:

      file1 = open('write_file_test.txt','w')
      day_str = input('How many days? [default 1] ')
      while not day_str.isdigit() and len(day_str) != 0:
        print('Please enter digits')
        day_str = input('How many days? [default 1] ')

      if len(day_str) == 0:
        # set default to 1 day
        total_days = 1
      else:
        total_days = int(day_str)

      print('total_days=', total_days)

      for day in range(1, total_days+1):
        sales_str = input('Enter sale amount for: ' + str(day) + ' ')
        while not sales_str.isdigit():
          sales_str = input('Not a digit, enter sale amount for: ' + str(day) + ' ')

        sales = float(sales_str)
        file1.write(str(sales) + '\n')
      file1.close()

    except Exception as err:
      print(err)

    else:
      print()
      file2 = open('write_file_test.txt')
      for data in file2:
        amount = float(data)
        print(amount)
      file2.close()

    # except ValueError as err:
    #   print(err)
    
    # except IOError as err:
    #   print(err)

    # except Exception as err:
    #   print(err)

    finally:
      print('clean up')
      file1.close()

    print('test.txt check end of line')
    file3 = open('test.txt', 'r')
    line = file3.readline().rstrip('\n')
    while line != '':
      print(line)
      line = file3.readline().rstrip()
    file3.close()

    print('test.txt preferred loop and list each line with split')
    file3 = open('test.txt', 'r')
    for data in file3:
      mylist = data.split(',')
      print(mylist)
    file3.close()

    print()
    file4 = open('write_file_test.txt', 'r')
    for data in file4:
      print(data.rstrip('\n'))
      print(float(data))

    file4.close()

    file5 = open('test1.txt', 'r')
    for data in file5:
      print(data.rstrip('\n'))

    file5.close()

  def list_exercise(self) -> None:
    ""
    print('************** list_exercise')      
    a = [1,2,3,4,5]
    print('a=', a, ' len=',len(a))
    b = range(5)
    print('b=',b)
    for i in b:
      print(i)

    c = []
    c.append(0)
    print('c=',c)

    file1 = open('test2.txt','r')
    mycontents = file1.readlines()
    file1.close()

    print('mycontents=', mycontents, type(mycontents))
    print()
    for i in range(len(mycontents)):
      mycontents[i] = mycontents[i].rstrip('\n')

    print('1')
    print(mycontents)    

    # index = 0
    # while index < len(mycontents):
    #   mycontents[index] = int(mycontents[index])
    #   index += 1

    for i in range(len(mycontents)):
      mycontents[i] = int(mycontents[i])

    print()
    print(mycontents)

    print('2')
    file2 = open('test.txt','r')
    mylist = list(file2)
    row_list = []
    for me in mylist:
      print(me.rstrip('\n'))

    file2.close()

  def factorial(self, num):    
    ""
    print('************** factorial:')    
    print('num=', num)
    f = 1
    i = 1
    while i <= num:
      f *= i
      i += 1

    print('result=', f)

def main():
  print ("exercise3.py")

  myobj = Exercise3(10,20,"Henry Jia")

  r1,r2,r3,r4 = myobj.test_print_pattern()
  print('result=', r1, r2, format(r3,'.2f'), format(r4, '.3f'))
  print('result=', format(math.sqrt(r1), '.2f'), format(math.sqrt(r2), '.2f'), format(math.sqrt(r3),'.2f'), format(math.sqrt(r4), '.3f'))

  myobj.file_read_write_exercise()
  myobj.list_exercise()

  myobj.factorial(5)

if __name__ == "__main__":
  main()