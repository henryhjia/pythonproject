"""
leetcode program
August 2023
"""
from modules import common_module

def validate_palindrome():
  """
  """
  common_module.print_function(validate_palindrome)

  s = "5 man, a plan, a canal: Panam5"

  lower_str = ''

  for c in s:
    if c.isalnum():
      lower_str += c.lower()
  print(s)
  print(lower_str)

  if lower_str == lower_str[::-1]:
    print(True)
  else:
    print(False)

def validate_palindrome2() -> bool:
  """
  """
  s = "A man, a plan, a canal: Panama"
  lower_str = ''
  for c in s:
    if c.isalnum():
      lower_str += c.lower()

  len_lower_str = len(lower_str)
  print(lower_str)
  print('len_lower_str=',len_lower_str)
  half = len_lower_str // 2
  print('half=',half)

  for i in range(half):
    print('i=',i, lower_str[i], lower_str[len_lower_str - i - 1])
    if lower_str[i] != lower_str[len_lower_str - i - 1]:
      return False
    
  return True

def best_time_buy_sell_stock():
  """
  You are given an array prices where prices[i] is the price of a given stock on the ith day.
  You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
  Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
  """
  common_module.print_function(best_time_buy_sell_stock)

  prices = [2,4,1]
  # prices = [3,2,6,5,0,3]
  prices = [7,1,5,3,6,4]

  max_p = prices[0]
  min_p = prices[0]
  min_index = 0
  max_index = 0

  max_diff = 0

  if len(prices) <= 1:
    return 0
  
  if len(prices) == 2:
    if prices[0] < prices[1]:
      return prices[1] - prices[0]
    else:
      return 0

  for i in range(len(prices)):
    # need to calculate the min
    # need to calculate the maximum difference
    diff = prices[i] - min_p
    if diff > max_diff:
      max_diff = diff
    if prices[i] < min_p:
      min_p = prices[i]  

    print('max_diff=', max_diff, 'min_p=', min_p)

def validate_parenthese_method2(s) -> bool:
  """
  use map(dictionary) and stack(list)
  """
  paren_map = {
    ')':'(',
    ']':'[',
    '}':'{'
  }

  stack = []

  for c in s:  
    if c not in paren_map: # is character '(' or '[' or '{'
      stack.append(c)
    else:
      if not stack:
        return False
      elif stack.pop() != paren_map[c]:
        return False   
    
  return False if stack else True

def validate_parenthese(s) -> bool:
  """
  """
  stack = []

  for c in s:
    if c=='(' or c=='[' or c=='{':      
      stack.append(c)
    elif c==')':
      if not stack:
        return False
      elif stack.pop() != '(':
        return False
    elif c==']':
      if not stack:
        return False
      elif stack.pop() != '[':
        return False    
    elif c=='}':
      if not stack:
        return False
      if stack.pop() != '{':
        return False    
    
  if len(stack) != 0:
    return False
    
  return True
  
def validate_parenthese_driver() -> None:
  """
  """
  common_module.print_function(validate_parenthese_driver)

  inlist = [
    '(]',
    '()',
    '{[]}',
    '([)]',
    '()[]{}',
    '()[]',
    '((',
    '){',
  ]
  print(inlist)

  for s in inlist:
    print(f'{s:10s} {validate_parenthese_method2(s)}')

def binary_search():
  """
  """
  common_module.print_function(binary_search)
  target = 5
  
  nums=[1,2,3,4,5,6,7,8,9,10,11,12,13]
  print(nums)
  print('target=', target)
  nlen = len(nums)

  low = 0
  high = nlen - 1

  while low <= high:
    mid = (low + high)//2
    if nums[mid] == target:
      return mid
    if nums[mid] < target:
      low = mid + 1
    else:
      high = mid - 1

  return -1

class Node:
  def __init__(self, val=0, next=None):
    self.value = val
    self.next = next
    

def singly_linked_list():
  """
  """
  common_module.print_function(singly_linked_list)

  node1 = Node(10)
  node2 = Node(20)
  node3 = Node(30)

  node1.next = node2
  node2.next = node3

  mynode = node1
  while mynode != None:
    print('node value=', mynode.value)
    mynode = mynode.next

def reverse_linked_list():
  """
  """
  common_module.print_function(reverse_linked_list)

  node1 = Node(10)
  node = node1
  node.next = Node(20)
  node = node.next
  node.next = Node(30)
  node = node1

  tmp = Node(node.value, None)
  print('initial obj value=', tmp.value)
  obj = None
  while node != None:
    
    # print('node value=', node.value, 'tmp value=', tmp.value)
    node = node.next
    if node != None:
      obj = Node(node.value, tmp)
      print('obj value=', obj.value, 'tmp value=', tmp.value)
      tmp = obj

  l1 = []
  while obj != None:
    # print(obj.value, end='')
    l1.append(obj.value)
    obj = obj.next

  print(l1)

def reverse_linked_list2():
  """
  """
  common_module.print_function(reverse_linked_list)

  node1 = Node(10)
  node = node1
  node.next = Node(20)
  node = node.next
  node.next = Node(30)
  node = node1

  prev = None

  while node != None:
    tmp = node.next
    node.next = prev
    prev = node
    node = tmp

  while prev != None:
    print(prev.value)
    prev = prev.next

def combine_two_sorted_linked_list():
  """
  """
  common_module.print_function(combine_two_sorted_linked_list)

  node1 = Node(1)
  node2 = Node(2)
  node3 = Node(4)
  node1.next = node2
  node2.next = node3
  list1 = node1

  node4 = Node(1)
  node5 = Node(3)
  node6 = Node(4)
  node4.next = node5
  node5.next = node6
  list2 = node4

  if list1 == None and list2 != None:
    return list2
  elif list1 != None and list2 == None:
    return list1
  elif list1 == None and list2 == None:
    return None
  
  head1 = list1
  head2 = list2

  if list1.value > list2.value:
    head1 = list2
    head2 = list1
  
  new_list = head1

  while head1 != None:
    if head1.next != None:
      if head1.next.value > head2.value:
        tmp = head1.next
        head1.next = head2
        head1 = head2
        head2 = tmp
      else:
        head1 = head1.next
    else:
      head1.next = head2
      return new_list
  
  return new_list

def frequent_element():
  """
  """
  common_module.print_function(frequent_element)

  nums = [1,1,1,2,2,3]
  # nums = [-1,-1]
  k = 2
  print(nums)

  if len(nums) <= 1:
    return nums

  mydict = {}

  for i in range(len(nums)):
    if nums[i] not in mydict:
      mydict[nums[i]] = 1
    else:
      mydict[nums[i]] += 1

  sorted_list = sorted(mydict.items(), key=lambda x:x[1], reverse=True)
  print(sorted_list)
  
  for i in range(k):
    print(sorted_list[i][0])



def main() -> None:

  validate_palindrome()

  print(validate_palindrome2())

  best_time_buy_sell_stock()

  validate_parenthese_driver()

  print('Index of found target=', binary_search())

  # singly_linked_list()

  reverse_linked_list2()

  node = combine_two_sorted_linked_list()
  while node != None:
    print(f'{node.value} ', end='')
    node = node.next

  print()

  frequent_element()

if __name__ == '__main__':
  main()


