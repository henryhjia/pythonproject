#!/use/bin/python3
"""
Reverse list
@reverselist

reverse a list : three methods
1. manual
2. slicing
3. list.reverse() method - in place reverse
"""

class ReverseTester:
  """
  @brief
  """

  def __init__(self) -> None:
    """
    @brief constructor
    """
    pass

  def reverse_list_by_coding(self, in_list: list) -> list:
    """

    """
    print('\n*********** reverse_list_by_coding()')

    out_list = []
    list_size = len(in_list)

    for i in range(list_size-1, -1, -1):
      out_list.append(in_list[i])

    return out_list

  def reverse_list_using_slicing(self, in_list: list) -> list:
    """
    A copy of a reversed list is generated
    """
    print('\n*********** reverse_list_using_slicing()')
    print('original list=', in_list)
    out_list = in_list[::-1]

    print('reversed list=', out_list)

    return out_list

def main() -> int:
  """
  """
  me = ReverseTester()

  # reverse list 
  list1 = [2,4,5,8]
  list2 = me.reverse_list_by_coding(list1)
  print('original list=', list1)
  print('reversed list=', list2)

  print('\n*********** reverse_list by list.reverse(), original list is reversed')
  print('original list=', list1)
  list1.reverse()  
  print('reversed list=', list1)

  list3 = me.reverse_list_using_slicing(list1)

if __name__ == '__main__':
  main()
