#!/use/bin/python3
"""
code signl program
August 2023
"""
from datetime import datetime
from datetime import timedelta
import pytz
import re
from Complex import Complex
from Points import Points
from functools import reduce
from fractions import Fraction

Gl_div = '+'*10

def print_function(function_name, parameter=''):
  """
  """
  print(f'{Gl_div} {function_name} for {parameter}')

def two_sums(nums: list[int], target:int) -> list[int]:
  """
  """
  function_name = two_sums
  print(f'{Gl_div} {function_name}')
  sum = 0
  result = []
  for i in range(len(nums)):
    sum = nums[i] + nums[i+1]
    if sum == target:
      result.append(i)
      result.append(i+1)
      break

  print(result)
  return result

def century_tester(year):
  """
  """
  function_name = century_tester
  print(f'{Gl_div} {function_name} for {year}')

  result = 0

  if year % 100 != 0:
    result = year//100 + 1
  else:
    result = year//100

  print(result)
      
def palindrome_tester(in_str):
  """
  """
  result = False
  function_name = palindrome_tester
  print(f'{Gl_div} {function_name} for {in_str}')

  if in_str == in_str[::-1]:
    result = True
  else:
    result = False
  
  print(result)

def interesting_polygon(n):
  """
  """
  function_name = interesting_polygon
  print(f'{Gl_div} {function_name} for {n}')
  sum = 0
  center_length = n*2 -1
  for i in range(1, center_length+1):
    sum += 1

  sum1 = 0
  for j in range(center_length-2, 0, -2):
    sum1 += j

  sum += sum1*2
  print('total=', sum)

def almost_increase_sequence(alist):
  """
  """
  print_function(almost_increase_sequence, alist)

  result = True

  if len(alist) == 1:
    return True
  
  if len(alist) == 2:
    if alist[1] >= alist[0]:
      return True
    else:
      return False
  
  # length >= 3
  result1 = True
  result2 = True
  blist = [] + alist
  for i in range(len(alist)-1):
    if alist[i+1] < alist[i]:
      del alist[i+1]
      break
    
d=c
  for i in range(len(alist)-1):
    if alist[i+1] <= alist[i]:
      result1 = False
    
  for i in range(len(blist)-1):
    if blist[i+1] < blist[i]:
      del blist[i]
      break

  for i in range(len(blist)-1):
    if blist[i+1] <= blist[i]:
      result2 = False

  return result1 or result2

def matrix_element_sum():
  """
  """
  print_function(matrix_element_sum)

  # matrix = [[0,1,1,2],
  #           [0,5,0,0],
  #           [2,0,3,3]]

  matrix = [[1,1,1,0],
            [0,5,0,1],
            [2,1,3,10]]            

  num_row = len(matrix)
  num_col = len(matrix[0]) if matrix else 0

  print(num_row, num_col)

  sum = 0
  remember_row_index = num_row - 1

  a = []
  for r in range(num_row):
    for c in range(num_col):
      print(f'{matrix[r][c]} ', end='')
      if matrix[r][c] == 0:
        a.append([r,c])
    print()

  print(a)
  flag = True

  for r in range(num_row):
    for c in range(num_col):
      if matrix[r][c] != 0:
        flag = True
        print(r,c)
        for i in a:
          if i[1] == c and i[0] < r:
            flag = False
        if flag == True:
          sum += matrix[r][c]

  print(sum)

def common_character_count():
  """
  s1 = "aabcc"
  s2 = "adcaae"

  slotution(s1,s2) = 3
  two common characters 'a' and one common character 'c'
  """
  s1 = "aabcc"
  s2 = "adcaae"

  d1={}
  d2={}

  for i in s1:
    if i in d1:
      d1[i] += 1
    else:
      d1[i] = 1

  for i in s2:
    if i in d2:
      d2[i] += 1
    else:
      d2[i] = 1

  sum = 0

  print(d1)
  print(d2)

  for key, value in d1.items():
    if key in d2:
      if value < d2[key]:
        sum += value
      else:
        sum += d2[key]

  print('common characters= ', sum)

def all_longest_string():
  """
  """

  a = ["aba", "aa", "ad", "vcd", "aba"]
  l = []
  l2 = []
  result = []

  for i in a:
    l.append(len(i))

  max_value = max(l)
  print('max=', max_value)

  for i in a:
    l2.append([i,len(i)])

  print(l2)

  for i in l2:
    if i[1] == max_value:
      result.append(i[0])

  print(result)

def is_lucky():
  """
  Given a nnumber (even number of digit)
  if the sum of the first half == sum of the second half, 
  then it is a lucky number
  """
  n = 1230

  str_n = str(n)

  l1 = len(str_n)
  l2 = int(l1/2)
  print(l1,l2)

  s1 = 0
  s2 = 0

  for i in range(0, l2):
    s1 += int(str_n[i])
    print(i, str_n[i], s1)

  for i in range(l2, l1):
    s2 += int(str_n[i])
    print(i, str_n[i], s2)

  print(s1,s2)

def sort_by_height():
  """
  a = [-1,150,190,170,-1,-1,160,180]
  sorted result:
  b = [-1,150,160,170,-1,-1,180,190]
  """
  a = [-1,150,190,170,-1,-1,160,180]

  i1 = []
  sum1 = 0

  for i in range(len(a)):
    print(a[i])
    if a[i] == -1:
      i1.append(i)
      sum1 +=1

  b=sorted(a)

  print(sum1)
  for i in range(sum1):
    b.remove(-1)
  print(i1)
  print(b)

  c=[]
  j=0
  for i in range(len(a)):
    if a[i] == -1:
      c.append(a[i])
    else:
      c.append(b[j])
      j += 1

  print(c)

def reverse_in_parenthese():
  """
  """
  print_function(reverse_in_parenthese)

  # a = "(bar)"

  # a = "foo(bar)baz"
  # b = foorabbaz

  # a = "foo(bar)baz(blim)"
  # b = "foorabbazmilb"

  a = "foo(bar(baz))blim"
  # b = "foobazrabblim"

  b = ''
  # pattern = r'\((.*?)\)'
  # match = re.search(pattern, a)

  # print(a)
  # print(match.group(0))
  # print(match.group(1))

  p_index_l = []
  p_index_r = []

  for i in range(len(a)):
    if a[i] == '(':
      p_index_l.append(i)

  for i in range(len(a)):
    if a[i] == ')':
      p_index_r.append(i)

  print(p_index_l)
  print(p_index_r)


  # paran_set = set()

  str_len=len(a)
  # for i in range(str_len):
  #   if a[i] == '(' or a[i] == ')':
  #     continue
  #   elif i < p_index_l[0] or i > p_index_r[0]:
  #     b += a[i]
  #   else:
  #     b += a[str_len-1-i]

  left = False

  # for i in range(str_len):
  #   if left == False and a[i] != '(':
  #     b += a[i]
  #   if a[i] == '(' and left == False:
  #     left = True
  #   if left == True:



  print(b)

def remove_compare_string():
  """
  This involves to remove character from a string
  using string.replace() method
  @removestring

  Given two strings s and t, both consisting of lower case English letters
  and digits, your task is to calculate how many ways exactly one digit could be
  removed frrom one of the strings so that s is lexicographically smaller than t
  after the removal.
  """
  print_function(remove_compare_string)

  # s="ab12c"
  # t="1zz456"
  s="ab12c"
  t="ab24z"

  l1=[]
  sum = 0

  for i in range(len(s)):
    if s[i].isdigit():
      print(s[i])
      r1 = s[i]
      m1 = s.replace(r1,"")
      l1.append(m1)
      if m1 < t:
        sum +=1

  for i in range(len(t)):
    if t[i].isdigit():
      print(t[i])
      r1 = t[i]
      m1 = t.replace(r1,"")
      l1.append(m1)
      if m1 > s:
        sum +=1

  print(l1)
  print(sum)

def sum_array():
  """
  Given an array of positive integers a, your task is to calculate the sum of
  every possible a[i]*a[j], where a[i]*a[j] is the concatenation of the string
  representations of a[i] and a[j] respectively.
  """
  print_function(sum_array)

  # a = [10,2]
  # a = [8]
  a = [1,2,3]

  sum = 0
  for i in range(len(a)):
    for j in range(len(a)):
      tmp_str = str(a[i]) + str( a[j])
      sum += int(tmp_str)
      print(a[i], a[j], tmp_str, sum)

  print('prod=', sum)  

def list_circular_slicing():
  """
  @circularslicing
  """
  print_function(list_circular_slicing)

  a = [1,0,2,4,7,3]

  list_len = len(a)
  size = 4
  print(a)
  b = []
  for i in range(list_len):
    if i <= list_len - size:
      start = i
      end = i + size
      b = a[start:end]
    else:
      end = size - (list_len - i)
      b = a[i:list_len] + a[0:end]

    print('i=',i, 'b=', b)


def main() -> int:

  # two sum tester
  two_sums([2,7,11,15], 9)
  two_sums([3,2,4], 6)
  two_sums([3,3], 6)

  # century tester:
  century_tester(20)
  century_tester(2023)
  century_tester(2000)

  palindrome_tester('aabaa')
  palindrome_tester('aabac')

  interesting_polygon(1)
  interesting_polygon(2)
  interesting_polygon(3)
  interesting_polygon(4)

  print(almost_increase_sequence([1,3,2]))
  print(almost_increase_sequence([1,3,2,1]))
  print(almost_increase_sequence([1,3,5,3,5]))  
  print(almost_increase_sequence([1,1]))  
  print(almost_increase_sequence([10,1,2,3,4,5]))  

  matrix_element_sum()

  all_longest_string()

  common_character_count()

  is_lucky()

  sort_by_height()
  
  reverse_in_parenthese()

  remove_compare_string()

  sum_array()

  list_circular_slicing()


if __name__ == '__main__':
  main()


