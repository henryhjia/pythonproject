#!/use/bin/python3
"""
Reverse list
@reverselist

reverse a list : three methods
1. looping
2. list.reverse() method - in place reverse
3. slicing
"""

import list_process_module

def main() -> None:
  """
  """
  me = list_process_module.ListProcessModule()

  # reverse list 
  list1 = [2,4,5,8]
  list2 = me.reverse_list_using_looping(list1)
  print('original list=', list1)
  print('reversed list=', list2)

  print('++++++++++ reverse_list by in-place reverse list.reverse(), original list is reversed')
  print('original list=', list1)
  list1.reverse()  
  print('reversed list=', list1)

  list3 = me.reverse_list_using_slicing(list1)
  print('original list=', list1)
  print('Reversed list=', list3)

if __name__ == '__main__':
  main()
