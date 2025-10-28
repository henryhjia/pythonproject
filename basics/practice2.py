#!/usr/bin/python3
# Henry Jia 2021
import os
import pickle
from enum import Enum

class Exercise2:
  """
  """

  def string_reverse(self) -> None:
    """
    """
    print('\n*********** string_reverse')  
    string='to be reversed'

    reverse_string=''

    str_len=len(string)
    for i in range(str_len):
      reverse_string += string[str_len-1-i]
    
    print('reverse str=', reverse_string)

    for i in reverse_string:
      print(i, end='')
    print()
    
    print('reverse string using slcing: ', string[::-1])
    mystr="hongjia"
    for i in mystr:
      print(i, end='')
    print()

    print('reverse string using slcing: ', mystr[::-1])

  def list_multiply(self) -> None:
    """
    """
    print('\n*********** list_multiply')    
    sample_list = [1,2,3,4,5,6]
    sum=0
    for i in sample_list:
      sum += i
    print('sum=', sum)

    mylen=len(sample_list)

    for i in range(0,mylen):
      sample_list[i] *= sum

    print(sample_list)

  def challenge1(self, n: int) -> None:
    """
    """
    print('\n*********** challenge1')
    str_n = str(n)
    print("str_n=", str_n)
    prod = 1
    sum = 0
    
    for st in str_n:
      print("str=",st)
      prod *= int(st)
      sum += int(st)

    print("Prod=", prod)
    print("Sum=", sum)

  def challenge2(self, p:str, s:str) -> None:
    """
    """
    print('\n*********** challenge2')
    # p contains 0 or 1
    # s contains low case letters
    total_match = 0
    
    if(len(p) != len(s)):
      print("two strings have different length")
      return

    else:
      print("processing")
      for i in range(len(p)):
        print(p[i]," ",s[i])
        if(p[i]=='0' and (s[i]=='a' or s[i] =='e' or
            s[i] == 'i' or s[i] == 'o' or
            s[i] == 'u' or s[i] == 'y')):
          total_match += 1

        elif (p[i]=='1' and s[i] != 'a' and s[i] != 'e' and
              s[i] != 'i' and s[i] != 'o' and
              s[i] != 'u' and s[i] != 'y'):
          total_match += 1
                                  
    print("total match=", total_match) 

  def challenge3(self) -> None:
    """
    """
    print('\n*********** challenge3')
    me = MyClass()
    me.open_file_find_lines_containing("token.txt",'Chicago')
    match_ct = me.number_of_lines_contained_in_token()
    print("match count=", match_ct)
    print()
    
    line_num = me.nth_instance_line_contains_token("token.txt",'New',1)
    print("nth line marching 'New'=", line_num)

    print()
    me.iterate_with_for_loop("token.txt")

  def readlines_test(self, filename: str) -> None:
    """
    """
    print('\n*********** readlines_test')
    myfile = open(filename, 'r')
    text = myfile.readlines()
    myfile.close()

    print('text=', text)
    num_list = []
    for tx in text:
        # num = int(tx.rstrip('\n'))
        num = int(tx)
        num_list.append(num)
        #print(num)
        
    print(num_list)
    print("min=",min(num_list))
    print("max=",max(num_list))
    num_list.sort()
    print("sorted=", num_list)
    num_list.reverse()
    print("reverse=", num_list)

  def test_sets(self) -> None:
    print('\n*********** test_sets')
    myset = set(['one','two','three'])
    print(myset)
    myset1=set('aaabc')
    print(myset1)
    myset1.remove('a')
    print(myset1)
    myset2=set([1,2,3,4,5,6])
    for var in myset2:
        print(var)
    if 1 in myset2:
        print("1 is in myset2")
    
  def readline_test(self, filename:str) -> None:
    """
    """
    print('\n*********** readline_test')    
    myfile = open(filename, 'r')
    text = myfile.readline()
    while(text !=''):
        text_new = text.rstrip('\n')
        print(int(text_new))
        text = myfile.readline()
    myfile.close()
    myfile = open(filename, 'r')
    for data in myfile:
      print('data=', int(data))

    myfile.close()
    
    myset = set(['one','two','three'])
    print(myset)

    myset1=set('abc')
    print(myset1)

  def test_serializing(self) -> None:
    """
    """
    print('\n*********** test_serializing')    
    outfile = open('output_data.dat', 'wb')
    phone_book= {'jia':'123-5678','jie':'555-8888'}
    print(phone_book)
    pickle.dump(phone_book, outfile)
    outfile.close()

    infile = open('output_data.dat','rb')
    pb = pickle.load(infile)
    print(pb)
    infile.close()

class MyClass:
  """
  """
  def __init__(self):
    """
    """
    self.match_count=0
    self.nth_instance=''
        
  def open_file_find_lines_containing(self, filename:str, token:str) -> None:
    """
    """
    match_count=0
        
    myfile = open(filename, 'r')

    line=myfile.readline()
    line = line.rstrip('\n')
    words = line.split()
    print('words=',words)
        
    for word in words:
      if(word == token):
        match_count += 1
                
    while line !='':
      line = myfile.readline()
      line = line.rstrip('\n')
      words = line.split()
      print('words=',words)
      for word in words:
        if(word == token):
          match_count += 1            

    self.match_count = match_count
        
    myfile.close()
        
  def number_of_lines_contained_in_token(self) -> None:
    """
    """
    return self.match_count

  def nth_instance_line_contains_token(self,filename:str, token:str,nth_instance: int) -> int:
    """
    """
    line_num_match = 0
    line_ct = 1
    myfile = open(filename, 'r')

    line=myfile.readline()
    line = line.rstrip('\n')
    words = line.split()
    print('words=',words)
        
    for word in words:
      if(word == token):
          line_num_match = 1
          self.nth_instance = line_num_match
          myfile.close()
          return self.nth_instance
                
      while line !='':
        line_ct += 1
        line = myfile.readline()
        line = line.rstrip('\n')

        words = line.split()
        print('words=',words)
        for word in words:
          if(word == token):
              line_num_match = line_ct
              self.nth_instance = line_num_match
              myfile.close()
              return self.nth_instance
        
    myfile.close()

  def iterate_with_for_loop(self, filename:str) -> None:
    """
    """
    print('filename=', filename)
    myfile = open(filename, 'r')
    for line in myfile:
      line = line.rstrip('\n')
      print(line)
    
    myfile.close()

class SystemTestEnum(Enum):
    system1 = 1
    system2 = 2
    system3 = 3
    system4 = 4
    system5 = 5
    system6 = 6
    system7 = 7

def main() -> int:
  try:
    ex = Exercise2()
    ex.string_reverse()
    ex.list_multiply()
    ex.challenge1(1234)
    ex.challenge2("0011","aucd")
    ex.challenge3()
    ex.readlines_test("records.txt")
    ex.readline_test("records.txt")
    ex.test_sets()

	  # Add one line for git
    ex.test_serializing()
    
    # Test enum
    print(SystemTestEnum)

    for j in SystemTestEnum:
      print(j)

    myinput = SystemTestEnum.system1
    print('item 1:', SystemTestEnum(1))
    name1 = 'system1'
    a1 = SystemTestEnum[name1]
    a2 = a1.value
    print('a1=',a1,'a2=',a2)
    match a2:
      case 1:
          print('case 1')
      case 2:
          print('case 2')
      case 3:
          print('case 3')
      case 4:
          print('case 4')
      case _:
          print('default case')


	# Add second line    
  except Exception as err:
    print("error happened, err=", err)
    # os.SOFTWARE

  os.EX_OK

if __name__ == '__main__':    
    main()