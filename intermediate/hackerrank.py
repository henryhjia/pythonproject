#!/use/bin/python3
"""
hackerrank program
July 2023
"""
import math
import cmath
import itertools
import calendar
from datetime import datetime
from datetime import timedelta
import pytz
import re
from Complex import Complex
from Points import Points
from functools import reduce
from fractions import Fraction

import common_module

from pathlib import Path

# Get the absolute path to the current script
CURRENT_DIR = Path(__file__).resolve().parent

# Go up one level to project root
PROJECT_ROOT = CURRENT_DIR.parent

# Point to the data directory
DATA_DIR = PROJECT_ROOT / "data"

# File path
input_file = DATA_DIR / "testcase1.txt"
output_file = DATA_DIR / "testcase1_out.txt"


def logo():
  # print('Input thickness of the logo: ')
  # thickness = int(input()) #This must be an odd number
  thickness = 5
  c = 'H'

  #Top Cone
  for i in range(thickness):
      print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))
      
  #Top Pillars
  for i in range(thickness+1):
      print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))
      
  #Middle Belt
  for i in range((thickness+1)//2):
      print((c*thickness*5).center(thickness*6))    

  #Bottom Pillars
  for i in range(thickness+1):
      print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))    

  #Bottom Cone
  for i in range(thickness):
      print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))


def wrap(string, max_width):
  new_str = ''
  end = len(string) - max_width

  for s in range(0,end,max_width):
      tmp_str = string[s:s+max_width] + '\n'
      new_str += tmp_str
      
  remain = len(string) % max_width
  remain_str = string[-remain:]  
  new_str += remain_str + '\n'

  return new_str

def print_formatted(number):
  """
  """
  print('print_formatted():')
  l1 = len(f'{number:d}')
  l2 = len(f'{number:o}')
  l3 = len(f'{number:X}')
  l4 = len(f'{number:b}')

  for i in range(1,number+1):
    print(f'{i:{l4}d} {i:{l4}o} {i:{l4}X} {i:{l4}b}')

def insert_dash_into_string(input_str):
   
  # insert '-' into strings
  new_str = ''
  for i in range(len(input_str)):
     new_str += input_str[i]
     if i < len(input_str) - 1:
        new_str += '-'

  return new_str

def print_rangoli(size):

  """
  3 -> 5 rows, 9 columns
  ----c----
  --c-b-c--
  c-b-a-b-c
  --c-b-c--
  ----c----

  5 -> 9 rows, 17 columns
  --------e--------
  ------e-d-e------
  ----e-d-c-d-e----
  --e-d-c-b-c-d-e--
  e-d-c-b-a-b-c-d-e
  --e-d-c-b-c-d-e--
  ----e-d-c-d-e----
  ------e-d-e------
  --------e--------

  10 -> 19 rows, 37 columns
  ------------------j------------------
  ----------------j-i-j----------------
  --------------j-i-h-i-j--------------
  ------------j-i-h-g-h-i-j------------
  ----------j-i-h-g-f-g-h-i-j----------
  --------j-i-h-g-f-e-f-g-h-i-j--------
  ------j-i-h-g-f-e-d-e-f-g-h-i-j------
  ----j-i-h-g-f-e-d-c-d-e-f-g-h-i-j----
  --j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j--
  j-i-h-g-f-e-d-c-b-a-b-c-d-e-f-g-h-i-j
  --j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j--
  ----j-i-h-g-f-e-d-c-d-e-f-g-h-i-j----
  ------j-i-h-g-f-e-d-e-f-g-h-i-j------
  --------j-i-h-g-f-e-f-g-h-i-j--------
  ----------j-i-h-g-f-g-h-i-j----------
  ------------j-i-h-g-h-i-j------------
  --------------j-i-h-i-j--------------
  ----------------j-i-j----------------
  ------------------j------------------
  """  
  # your code goes here
  alpha = 'abcdefghijklmnopqrstuvwxyz'
  sub_str = alpha[0:size]

  print(sub_str, 'size=', size)

  num_rows = size*2 -1
  num_cols = num_rows*2 -1
  print(f'num_rows={num_rows}, num_cols={num_cols}')
  left_size = num_cols//2
  print('left_size=', left_size)

  cur_str = ''
  upper_left_str = ''
  upper_right_str = ''
  first_line_left_size = num_cols // 2
  print('first line left size=', first_line_left_size)
  count = 0

  for i in range(len(sub_str)-1,-1,-1):
    cur_str = sub_str[i]
    upper_left_str += cur_str
    tmp_reverse = upper_left_str[::-1]
    upper_right_str = tmp_reverse[1::]

    # print left '-'
    for j in range(0,first_line_left_size - count):
      print('-', end='')

    # print main string
    upper_left_str_dash = insert_dash_into_string(upper_left_str)
    upper_right_str_dash = insert_dash_into_string(upper_right_str)

    if len(upper_left_str) > 1:
      print(upper_left_str_dash, '-', upper_right_str_dash, sep='', end='')
    else:
      print(upper_left_str, upper_right_str, sep='', end='')

    # print right '-'
    for j in range(0,first_line_left_size - count):
      print('-', end='')    

    print()
    count += 2

  count = 2
  lower_left_str = ''
  lower_right_str = ''
  for i in range(1, len(sub_str)):
    lower_left_str = upper_left_str[:-1*i]
    tmp_reverse = lower_left_str[::-1]
    lower_right_str = tmp_reverse[1::]    

    # print left '-'
    for j in range(0,count):
      print('-', end='')

    # print main string
    lower_left_str_dash = insert_dash_into_string(lower_left_str)
    lower_right_str_dash = insert_dash_into_string(lower_right_str)

    if len(lower_left_str) > 1:
      print(lower_left_str_dash, '-', lower_right_str_dash, sep='', end='')
    else:
      print(lower_left_str, lower_right_str, sep='', end='')
  
    # print right '-'
    for j in range(0,count):
      print('-', end='')
    print()
    count += 2

def capitalize(in_str):
  """
  """    
  words = in_str.split(' ')
  new_str = ''

  for i in words:
    for j in range(len(i)):
      if j == 0:
        new_str += i[0].upper()
      else:
        new_str += i[j]
    new_str += ' '

  print(new_str)

def mat_design(num_row, num_col):  
  """
  Size: 7 x 21 
  ---------.|.---------
  ------.|..|..|.------
  ---.|..|..|..|..|.---
  -------WELCOME-------
  ---.|..|..|..|..|.---
  ------.|..|..|.------
  ---------.|.---------
  
  Size: 11 x 33
  ---------------.|.---------------
  ------------.|..|..|.------------
  ---------.|..|..|..|..|.---------
  ------.|..|..|..|..|..|..|.------
  ---.|..|..|..|..|..|..|..|..|.---
  -------------WELCOME-------------
  ---.|..|..|..|..|..|..|..|..|.---
  ------.|..|..|..|..|..|..|.------
  ---------.|..|..|..|..|.---------
  ------------.|..|..|.------------
  ---------------.|.---------------  
  """


  for row in range(num_row):
    for col in range(num_col):
      print('-', sep='', end='')
    print()

def remove_duplicate_str(s):
  """
  """
  s2 = ''
  for i in s:
    if not i in s2:
      s2 += i

  return s2

def merge_the_tools(in_string, k):
  """
  """
  common_module.print_function(merge_the_tools, {in_string})
  str_len = len(in_string)
  num_sub_str = str_len//k

  # print(in_string, str_len, k, num_sub_str)

  s1 = ''
  s2 = ''
  
  for i in range(0,str_len,k):
    for j in range(k):
      s1 += in_string[i+j]
    s2 = remove_duplicate_str(s1)
    s1 = ''
    print(s2)

def set_discard_remove_pop():
  """
  use getattr() to use command in string representation
  """
  common_module.print_function(set_discard_remove_pop)

  s = set([1,2,3,4,5,6,7,8,9])
  num_cmd = 10
  cmdlist = ['pop', 'remove 9', 'discard 9','discard 8', 'remove 7', 'pop', 'discard 6','remove 5','pop','discard 5']

  print (cmdlist)

  for i in cmdlist:
    cm = i.split()
    if len(cm) > 1:
      arg = int(cm[1])
      getattr(s, cm[0])(arg)
    else:
      getattr(s, cm[0])()

  print(sum(s))

def set_union():
  """
  pay attentation of how to enter a number of digit, and then populate a set"
  input_string = input()
  numbers = [int(num) for num in input_string.split()]
  s1 = set(numbers)
    
  """
  n1 = 9
  s1 = set({'1','2','3','4','5','6','7','8','9'})
  # input_string = input()
  # numbers = [int(num) for num in input_string.split()]
  # s1 = set(numbers)

  n2 = 9
  s2 = set({'10','1','2','3','11','21','55','6','8'})

  # input_string = input()
  # numbers = [int(num) for num in input_string.split()]
  # s2 = set(numbers)

  print(s1)
  print(s2)

  s3 = s1.union(s2)
  print(s3)
  print(len(s3))

def collection_counter():
  """
  note:
  read 1 2 3 4 using:
  input_string = input()
  numbers = [int(num) for num in input_string.split()]

  read
  3
  1 10
  2 20
  3 30
  using:
  n2 = int(input())
  for i in range(n2):
    in_str = input()
    val_list = [int(num) for num in in_str.split()]

  """
  n1 = int(input('Enter a number:'))
  input_string = input('Enter a list of integers:')
  numbers = [int(num) for num in input_string.split()]
  l1 = list(numbers)

  print(l1)

  n2 = int(input('Enter another number:'))
  sum = 0
  for i in range(n2):
    in_str = input('Enter a pair of integer like this: 1 10:')
    val_list = [int(num) for num in in_str.split()]
    if val_list[0] in l1:
      sum += val_list[1]
      l1.remove(val_list[0])

  print(l1)
  print(sum)

def default_dict():
  """
  use default dict
  """

  from collections import defaultdict
  input_line = input('Enter two integers:')
  if len(input_line.split()) <=1:
    print('Please enter two integers')
    exit(1)
  n, m = map(int, input_line.split())

  print(n,m)
  d = defaultdict(list)

  for i in range(n):
    a = input('Enter a word in Group A:')
    d['Group_A'].append(a)

  list1 = []
  found = False

  list2 = []
  for i in range(m):
    b = input('Enter a word in group B:')
    list2.append(b)

  # print(list2)
  for i in range(len(list2)):
    for j in range(len(d['Group_A'])):
      if d['Group_A'][j] == list2[i]:
        list1.append(j+1)
        found = True
    
    if found:
      mystr = ''
      for k in list1:  
        mystr += str(k) + ' '
      print(mystr)  
      list1.clear()
    elif found == False:
      print(-1)
    # list1.clear()
    found = False
    # print()    

def default_dict_with_file():
  """
  """
  from collections import defaultdict

  list1 = []

  found = False
  d = defaultdict(list)  
  myfile = open(input_file, 'r')
  out_file = open(output_file, 'w')
  text = myfile.readline()

  i = 0
  while(text !=''):
    text_new = text.rstrip('\n')
    if i == 0:
      test_list = text.split(' ')
      n = int(test_list[0])
      m = int(test_list[1])
      print(n, m)
    else:
      # populate group A
      if i<=n:
        d['Group_A'].append(text_new)
      else:
        # check group B
        for k in range(n):
          if d['Group_A'][k] == text_new:
            list1.append(k+1)
            found = True
        # print result

        if found:
          mystr = ''
          for l in list1:  
            mystr += str(l) + ' '
          mystr = mystr.rstrip(' ')
          print(mystr)
          mystr += '\n'
          out_file.write(mystr)
          list1.clear()
        elif not found:
          print('-1')
          out_file.write('-1\n')

    found = False        
    i+=1
    text = myfile.readline()
    
  print('total lines=', i)
  print('size of group a=', len(d['Group_A']))

  myfile.close()
  out_file.close()

def sort_company_logo(in_str):
  """
  this function sorts string,
  then sort dictionary by values
  """

  sorted_string = ''.join(sorted(in_str))
    
  my_dic = dict()
  
  print(sorted_string)

  for s in sorted_string:
      if s not in my_dic:
          my_dic[s] = 1
      else:
          my_dic[s] += 1
          
  print(my_dic)

  mylist = sorted(my_dic.items(), key=lambda x:x[1], reverse=True)
  print('sorted dictionary view=', mylist)
  sorted_dict = dict(mylist)

  print(sorted_dict)

  for key, value in sorted_dict.items():
    print(key, value)

def itertool_prod():
  """
  a = [1, 2]
  b = [3, 4]
  result:
  c = (1,3) (1,4) (2,3) (2,4)
  """
  common_module.print_function(itertool_prod)

  a = [1, 2]
  b = [3, 4]

  for i in a:
    for j in b:
      s1 = tuple([i,j])
      print(s1, end='')
      print(' ', end='')

  print()

def set_symmetric_difference():
  """
  Convert list of character to list of integer

  >> a = raw_input()
  5 4 3 2
  >> lis = a.split()
  >> print (lis)
  ['5', '4', '3', '2']
  If the list values are all integer types, use the map() method to convert all the strings to integers.

  >> newlis = list(map(int, lis))
  >> print (newlis)
  [5, 4, 3, 2]
  
  
  """

  set1 = {2,4,5,9}
  set2 = {2,4,11,12}

  set3 = set1 ^ set2
  sorted_list = sorted(set3)

  for i in sorted_list:
    print(i)

def happyness_count():
  """
  
  """

  input_line = input('Enter two integers n and m: ')
  n, m = map(int, input_line.split())
  print(f'n={n} m={m}')

  input_line = input(f'Enter list n with {n} elements: ')
  list_str = input_line.split()
  list_n = list(map(int, list_str))

  happyness_count = 0

  # read A
  input_line = input(f'Enter array A with {m} elements: ')
  list_str = input_line.split()
  list_A =list(map(int, list_str))
  set_A = set(list_A)
  print(set_A)

  for i in list_n:
      if i in set_A:
          happyness_count += 1
          
  # read B
  input_line = input(f'Enter array B with {m} elements: ')
  list_str = input_line.split()
  list_B =list(map(int, list_str))
  set_B = set(list_B)
  print(set_B)

  for i in list_n:
      if i in set_B:
          happyness_count -= 1
          
  print(f'Happyness count: {happyness_count}')
    
def door_mat():
  """
  """
  # input_line = input()
  # n, m = map(int, input_line.split())
  n=11
  m=33
  row_center = n//2
  col_center = m//2
  dash_count = int((m-7)/2)
  
  print(n,m)
  print(row_center, col_center, dash_count)

  for i in range(n):
      if i < row_center:
        dec_num = i*2 + 1
        # print(dec_num)
        dash_num = int((m - dec_num*3)/2)
        # print(dash_num)
        for j in range(dash_num):
          print('-', end='')
        for j in range(dec_num):
          print('.|.', end='')
        for j in range(dash_num):
          print('-',end='')
        print()
      elif i == row_center:
        for j in range(dash_count):
            print('-', end='')
        print('WELCOME', end='')
        for j in range(m-dash_count, m):
            print('-', end='')
        print()
      elif i > row_center:
        dec_num = (n - i)*2 - 1 
        dash_num = int((m - dec_num*3)/2)
        for j in range(dash_num):
          print('-', end='')
        for j in range(dec_num):
          print('.|.', end='')
        for j in range(dash_num):
          print('-',end='')        
        print()
  print()

def set_mutation():
  """
  """
  na = int(input('Enter number of element in set A: '))
  in_str = input(f'Enter {na} integers in set A: ')
  list_str = in_str.split()
  list_int = list(map(int, list_str))
  set_A = set(list_int)
  print('set_A=', set_A)
  n = int(input('Enter total number of operations: '))

  for i in range(n):
    cmd_str = input('Enter command and number of element in set B: ')
    cmd_list = cmd_str.split()
    cmd = cmd_list[0]
    num_elem = cmd_list[1]
    data_str = input(f'Enter {num_elem} of integers for set B: ')
      
    list_data_str = data_str.split()
    list_data_int = list(map(int, list_data_str))
    set_B = set(list_data_int)
    print('set_B=', set_B)
    print(cmd)
    getattr(set_A, cmd)(set_B)
    print('set_A=', set_A)

  print('Sum of the set A=', sum(set_A))  

def polar_coordinates():
  """
  Use cmath to process complex number
  """
  in_str = 1 + 2j
  complex_num = complex(in_str)
  print(complex_num)

  r=abs(complex(complex_num))
  phase=cmath.phase(complex_num)

  print('r=', r)
  print('phase=', phase)

def print_triangle():
  """
  """
  common_module.print_function(print_triangle)

  # for i in range(1,int(input('Enter a number: '))): #More than 2 lines will result in 0 score. Do not leave a blank line also
  for i in range(1,5):
      print(((10 ** i - 1) // 9) * i)

  # for i in range(1,int(input('Enter a number: '))): #More than 2 lines will result in 0 score. Do not leave a blank line also
  for i in range(1,5):
      print(((10 ** i - 1) // 9) * ((10 ** i - 1) // 9))

def iter_tools():
  """
  """

  numbers = itertools.count(start=1)
  print('numbers=', numbers)
  for i in range(10):
    print(next(numbers))

  a = list(itertools.permutations(['H','A','C','K'], 2))
  b = sorted(a)
  for i in b:
    for j in i:
      print(j, end='')
    print()

def compress_string():
  """
  """
  common_module.print_function(compress_string)

  a='1222311'
  print(a)

  result_list = []

  count = 1
  for i in range(len(a)):
    if i<len(a)-1:
      if a[i] == a [i+1]:
        count += 1
      else:
        my_tuple = (count, int(a[i]))
        copy_tuple = tuple(my_tuple)
        result_list.append(copy_tuple)

        count = 1
    else:
      my_tuple = (count, int(a[i]))
      copy_tuple = tuple(my_tuple)
      result_list.append(copy_tuple)
 
  for i in result_list:
    print(f'{i} ', end='')
  
  print()

def print_calendar():
  """
  """
  common_module.print_function(print_calendar)

  print(calendar.TextCalendar(firstweekday=6).formatyear(2023))

  day = calendar.weekday(2023,8,9)

  print(day)

  weekday_dict = {0:'MONDAY', 1:'TUESDAY', 2:'WEDNESDAY', 3:'THURSDAY', 4:'FRIDAY', 5:'SATURDAY', 6:'SUNDAY'}
  print(weekday_dict[day])

def datetime_module():
  """
  1. Populate datetime object using string with format
  2. Calculate time difference in seconds
  @datetime
  """
  common_module.print_function(datetime_module)

  current_datetime = datetime.now()
  print('current time=', current_datetime)

  t1f = current_datetime.strftime('%Y-%m-%d %H:%M:%S')
  # print('current time (Formated)=', t1f)

  later_time = current_datetime + timedelta(weeks=1)
  print('later time  =', later_time)  
  print(later_time - current_datetime)

  t1 = datetime.strptime('2023-08-09 15:30:00', '%Y-%m-%d %H:%M:%S')
  print(f'parsed date= {t1}')

  t2 = datetime.strptime('2023-08-09 16:30:00', '%Y-%m-%d %H:%M:%S')
  print(f'parsed date= {t2}')

  utc_now = datetime.now(pytz.utc)
  # print(format('utc now=', '10s'), utc_now)

  diff = t2 - t1
  print('diff=', diff)

  t1 = datetime.strptime('Sun 10 May 2015 13:54:36 -0700', '%a %d %b %Y %H:%M:%S %z')
  t2 = datetime.strptime('Sun 10 May 2015 13:54:36 -0000', '%a %d %b %Y %H:%M:%S %z')
  t1t = t1.timestamp()
  t2t = t2.timestamp()
  print('t1 timestamp=', t1t)  
  print('t2 timestamp=', t2t)
  diff = t1t - t2t
  print('diff =', diff)
  print(f'diff = {diff:.0f}')

  t1 = datetime.strptime('Sat 02 May 2015 19:54:36 +0530', '%a %d %b %Y %H:%M:%S %z')
  t2 = datetime.strptime('Fri 01 May 2015 13:54:36 -0000', '%a %d %b %Y %H:%M:%S %z')
  t1t = t1.timestamp()
  t2t = t2.timestamp()
  print('t1=',t1)
  print('t2=',t2)
  print('t1 timestamp=', t1t)  
  print('t2 timestamp=', t2t)
  diff = t1t - t2t
  print('diff =', diff)
  print(f'diff = {diff:.0f}')

def regx_tester():
  """
  """

  reg1 = '.*\+'
  reg2 = '.*+'

  try:
    re.compile(reg1)
    print(True)
  except re.error as e:
    print(False)

  try:
    re.compile(reg2)
    print(True)
  except re.error as e:
    print(False)

def complex_calculation():
  """
  """
  function_name = complex_calculation
  print(f'{Gl_div} {function_name}')

  c = map(float, input('Enter 1st complex number: real imaginary: ').split())
  d = map(float, input('Enter 2st complex number: real imaginary: ').split())

  x = Complex(*c)
  y = Complex(*d)

  print(x)
  print(y)
  print(x+y)
  print(x-y)
  print(x*y)
  print(x/y)
  print(x.mod())
  print(y.mod())

def torsional_angle():
  """
  """
  common_module.print_function(torsional_angle)

  points = list()
  # for i in range(4):
  #     a = list(map(float, input().split()))
  #     points.append(a)

  # print(points)
  # points = [[0,4,5],[1,7,6],[0,5,9],[1,7,2]]

  points = [[5.0,8.8,9.0],[4.0,-1.0,3.0],[7.0,8.7,3.3],[4.4,5.1,6.3]]

  a, b, c, d = Points(*points[0]), Points(*points[1]), Points(*points[2]), Points(*points[3])
  print('type a=', type(a))
  x = (b - a).cross(c - b)
  y = (c - b).cross(d - c)

  try:
    angle = math.acos(x.dot(y) / (x.absolute() * y.absolute()))
    print("%.2f" % math.degrees(angle))
  except Exception as e:
    print(e)

def buildins_zipped():
  """
  use zip():
  l2 = [[1,1],[2,2]]
  l3 = list(zip(*l2))
  print(l3):
  [(1,2),(1,2)]
  """
  # n,x=map(int,input().split())
  # print(n,x)
  # l2 = []
  # for i in range(x):
  #   l1 = list(map(float, input().split()))
  #   l2.append(l1.copy())

  n=2
  x=2
  l2 = [[1,1],[2,2]]
  l3 = list(zip(*l2))
  print(l3)
  sum = 0
  for i in l3:
    for j in i:
      sum += j
    print(sum/x)
    sum = 0

def is_palindromic_integer(num):
    # Convert the integer to a string
    num_str = str(num)
    
    # Compare the string with its reverse
    return num_str == num_str[::-1]

def test_any_all():
  """
  """
  common_module.print_function(test_any_all)

  l1 = [1, 23, 121, 5, 9]

  test1 = True
  for i in l1:
    if i < 0:
      test1 = False

  test2 = True
  for i in l1:
    if not is_palindromic_integer(i):
      test2 = False

  print(all(num>0 for num in l1))
  print(all(is_palindromic_integer(num) for num in l1))

  # method 2:
  is_palindromic = lambda num: str(num) == str(num)[::-1]
  print((all(num>0 for num in l1)) and (any(is_palindromic(num) for num in l1)))

def sort_string_alph_digit():
  """
  """
  common_module.print_function(sort_string_alph_digit)

  s = 'Sorting1234'
  sorted_str = sorted(s, key=lambda x: (x.isdigit(), x.isdigit() and int(x) % 2 == 0, x.isupper(), x))

  for i in sorted_str:
    print(f'{i}', end='')

  print()

def eval_test():
  """
  Input:
  1 4
  x**3 + x**2 + x + 1

  Output:
  True

  """
  function_name = eval_test
  print(f'{Gl_div} {function_name}')

  x, k = map(int, input('Enter 1 4: ').split())
  command_Str = input('Enter x**3 + x**2 + x + 1: ')

  result = eval(command_Str)
  if result == k:
      print(True)
  else:
      print(False)

def fibonacci(n):
    # return a list of fibonacci numbers
    fibonacci1 = lambda n: [0, 1] + [fibonacci(i)[-1] + fibonacci(i)[-2] for i in range(2, n)]
    
    result = fibonacci1(n)
    if n == 0:
      result = []
    elif n == 1:
      result = [0]

    return result

def fibonacci_lambda_map_tester():
  """
  """
  common_module.print_function(fibonacci_lambda_map_tester)

  cube = lambda x: x*x*x
  n=0
  print(list(map(cube, fibonacci(n))))

def fun(s):
  # return True if s is a valid email, else return False
  # Requirement:
  # It must have the username@websitename.extension format type.
  # The username can only contain letters, digits, dashes and underscores .
  # The website name can only have letters and digits .
  # The extension can only contain letters .
  # The maximum length of the extension is 3.

  pattern = r'^[\w-]+@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}$'
  return re.match(pattern, s) is not None

def filter_mail(emails):
    return list(filter(fun, emails))

def email_validation():
  """
  """
  function_name = email_validation
  print(f'{Gl_div} {function_name}')

  emails = ['iu89_in.plus@google.c', 'ill@google.com']
  filtered_emails = filter_mail(emails)
  print(filtered_emails)

def product(fracs):
    t = reduce(lambda x,y: x*y , fracs) # complete this line with a reduce statement
    return t.numerator, t.denominator

def reduce_tester():
    fracs = []
    for _ in range(int(input('Enter 3: '))):
        fracs.append(Fraction(*map(int, input('Enter two digit: (1,2)(3,4),(10,6) ').split())))
    result = product(fracs)
    print(result)
    print(*result)

def regular_expression_tester():
  """
  @regularexpression
  """
  common_module.print_function(regular_expression_tester)

  pattern = '^[+\-.]?(?:\d+\.\d+|\.\d+|\d+\.)$'

  s = '4.4'
  result = re.match(pattern, s) 
  if result != None:
    print(True)
  else:
    print(False)

  pattern = '^[+\-.]?(?:\d+\.\d+|\.\d+|\d+\.)$'

  regex_pattern = r"[\,\.]"	# Do not delete 'r'.

  print("\n".join(re.split(regex_pattern, '100,000,000.000')))

def group_tester():
  """
  """
  common_module.print_function(group_tester)

  #s = '..12345678910111213141516171820212223'
  s = '__commit__'

  found = False
  for i in range(len(s) - 1):
      if s[i].isalnum():
        if s[i] == s[i+1]:
            print(s[i])
            found = True
            break
      
  if found == False:
      print(-1)

def matching_string():
  """
  @regularexpression
  """
  common_module.print_function(matching_string)
  s = "1234"
  m = re.search(r'\d+','1234')
  print('start=', m.start())
  print('end=', m.end())

  # s= "aaadaa"
  # p = "aa"
  s = "jjhv"
  p = "z"

  s_len = len(s)
  p_len = len(p)
  print(s_len,p_len)
  matched = False

  for i in range(s_len-p_len+1):
    s1 = s[i:i+p_len]
    print(s1)
    m = re.search(p,s1)
    if m:
      meset = (m.start()+i, m.end()+i-1)
      print(meset)
      matched = True
      
  if matched == False:
    print(f'(-1,-1)')

def substitute_string():
  """
  @regularexpression
  """
  common_module.print_function(substitute_string)
  # s = "elif a*b > 10 || a/b < 1:"
  # s = "x|& &|&&||&& x"
  # s = "x &  & |& |  x"
  # s = "x|&&|&& &||| x"
  # s = "x||& &|&& & |x"
  # s = "x&& &    && &x"
  # s = "x|&&|&&&|&&&& &&&   &|&| x"
  # s = "x|&|& |   ||& ||  || ||&|x"
  # s = "x&&& ||&|&& & &&& &|| | &x"
  # s = "x  &|&&|&& |   ||&  |&&| x"
  # s = "x& | && | | ||& &||| | |&x"
  # s = "x& &&&&||&&  |&&& ||&&& |x"
  # s = "x& |&  &||&||&& &&&&&|&&|x"
  # s = "x & | & |||| || && &&&&||x"
  # s = "x&&|&&&   |& |&&|& || &| x"
  # s = "x||&|&& & || & &&& | | | x"
  # s = "x ||  |&& |||&&  |   &&  x"
  # s = "x|||| |& | &&|&&&|&| |&&&x"
  # s = "x&& &|  & |& & |  |&| &||x"
  # s = "x&|  & |  |&|&&&||&|&&& |x"
  # s = "x|&| &|&| ||&||| &&&||  |x"
  # s = "x |  &||&&  |& | | |&||  x"
  # s = "x   |& &|& &  |&  |  | |&x"
  # s = "x&| &|   &   &   & |  ||&x"
  # s = "x&||&|| &||| | |||   | ||x"
  s = "x&& &&& && && x || | ||\|| x"
  # s = "This is a test && and another && example && and more && text. || This is a test || and another || example || and more || text."

  # print(s)
  # updated_text = re.sub(r'(?<!&)(?<=\S) (&{2,}) (?=\S)(?! )', r' and ' * len(r'\1'), s)

  # # Substitute ' || ' with ' or '
  # updated_text = re.sub(r'(?<!\|)(?<=\S) (\|{2,}) (?=\S)(?! )', r' or ' * len(r'\1'), updated_text)

  # print(updated_text)

  text = "jia hong 123 jiaa jjj"
  print(text)
  pattern = r'jia+'
  found = re.search(pattern,text)
  if found:
    print('found match:', found.group())
  else:
    print('no match')

  found = re.findall(pattern,text)
  print(found)

  # match = re.search(r'\w\w\w', 'abcd!!') 
  # if match:
  #   print(match.group())

  # print(s)
  # if " || " in s and " && " not in s:
  #   x = re.sub(r" \|\| ", " or ", s)
  #   print(x)
  # elif " && " in s and " || " not in s:
  #   x = re.sub(" \&\& ", " and ", s)
  #   print(x)
  # elif  " || " in s and " && " in s:
  #   x = re.sub(r" \|\| ", " or ", s)
  #   x1 = re.sub(r" \&\& ", " and ", x)
  #   print(x1)
  # else:
  #   print("no change",s)

  match = re.search(r'\d\s*\d\s*\d', 'xx1 2   3xx')
  if match:
    print(match.group())


def email_validation():
  """
  A valid email address meets the following criteria:

  It's composed of a username, domain name, and extension assembled in this format: 
  username@domain.extension
  The username starts with an English alphabetical character, and any subsequent 
  characters consist of one or more of the following: alphanumeric characters, -,., and _.

  The domain and extension contain only English alphabetical characters.
  The extension is 1, 2, or 3 characters in length.

  @emailvalidation
  @validateemail
  @regularexpression
  """
  common_module.print_function(email_validation)
  email_list = [
  '<alice-b@google.com>',
  '<Henry.jia_12@Gmail.com>',
  "<dexter@hotmail.cm>",
  "<virus!@variable.:p>",
  "<itsallcrap>",
  "<harsh_1234@rediff.in>",
  "<kunal_shin@iop.az>",
  "<matt23@@india.in>",
  '<.harsh_1234@rediff.in>'
  ]

  pattern = r'^<[a-zA-Z][a-zA-Z0-9-._]*@[a-zA-Z]+\.[a-z|A-Z]{1,3}>$'

  email_size = len(email_list)

  for str in email_list:
    match = re.search(pattern, str)
    if match:
      print(f'{str:30s} {match.group()}')  
    else:
      print(f'{str:30s} no match')

def phone_number_validation():
  """
  A valid mobile number is a ten digit number starting with a 7,8 or 9.
  @regularexpression
  @validatephoneumber
  @phonevalidation
  @phonenumbervalidation
  """
  common_module.print_function(phone_number_validation)

  pattern = r'^[7-9]\d{9}$'

  phone_list = [
    "9587456281",
    "1252478965",
    "87453231",
    "987rtd90fd",
    "131231",
    "85234789651"
  ]

  list_size = len(phone_list)

  for phone in phone_list:
    match = re.search(pattern, phone)
    if match:
      print(f'{phone:30s} {match.group()}')
    else:
      print(f'{phone:30s} no match')

def hex_color_match():
  """
  """
  text = "color: #FfFdF8; background-color:#aef;"
  pattern = r"#([A-Fa-f0-9]{3}|[A-Fa-f0-9]{6})"

  hex_colors = re.findall(pattern, text)

  print(hex_colors)

  pattern = r'[a-z]+='
  text = "<link rel='alternate' type='text/html' href='http://hackerrank.com/'/>"
  if text.count('1') <= 1:

    found = re.findall(pattern, text)
    if found:
      print(found)

def main() -> int:

  # print logo
  logo()

  # wrap string
  string = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
  max_width = 4
  result = wrap(string, max_width)
  print(result)
  
  print_formatted(99)

  print_rangoli(6)

  capitalize("jia hong")

  mat_design(7, 21)

  merge_the_tools('AABCAAADA', 3)

  set_discard_remove_pop()

  set_union()

  # collection_counter()
  # default_dict()

  default_dict_with_file()

  sort_company_logo('google')
  
  itertool_prod()

  set_symmetric_difference()

  # Interactive
  # happyness_count()

  # Interctive
  door_mat()

  # interactive
  # set_mutation()

  polar_coordinates()

  # Interactive
  print_triangle()

  iter_tools()

  compress_string()

  print_calendar()

  datetime_module()

  regx_tester()

  # Interactive
  # complex_calculation()

  torsional_angle()

  buildins_zipped()

  test_any_all()

  sort_string_alph_digit()

  # Interactive
  # eval_test()

  fibonacci_lambda_map_tester()

  email_validation()

  # Interactive
  # reduce_tester()

  regular_expression_tester()

  group_tester()

  matching_string()

  substitute_string()

  email_validation()

  phone_number_validation()

  hex_color_match()

if __name__ == '__main__':
  main()


