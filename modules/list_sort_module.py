#!/use/bin/python3
"""
Sort list
@sortlist

Two methods:
l2 = sorted(l1) - create a new list that is sorted
l1.sort() - in place sort

"""
import common_module

class SortListTester:
  """
  """
  def sort_sorted(self) -> None:
    """
    1. sorted()
    """
    common_module.print_function(self.sort_sorted)

    l1 = [10, 9,4,6,20,1]

    l2 = sorted(l1)
    print('original list=', l1)
    print('sorted list  =', l2)

    l1 = ['henry', 'claire', 'jean', 'maggie']
    l2 = sorted(l1)
    print('original list=', l1)
    print('sorted list  =', l2)

  def sort_in_place_sort(self):
    """
    2. sort() - in place sort
    """
    common_module.print_function(self.sort_in_place_sort)

    l1 = [10, 9,4,6,20,1]
    print('original list=', l1)
    l1.sort()
    print('sorted list  =', l1)

    l1 = ['henry', 'claire', 'jean', 'maggie']
    print('original list=', l1)
    l1.sort()
    print('sorted list  =', l1)

  def sort_integer_unique_mixed_data_type_in_list(self):
    """
    Given a list of different type, sort the integers in the list in asend order, 
    no duplicate
    Since it requires unique, a set is used
    """
    common_module.print_function(self.sort_integer_unique_mixed_data_type_in_list)

    myset = set()
    mylist = [3,2,1,10,6,7,2,1,"jia",'c']
    print('original list=')
    print(mylist)

    for elem in mylist:
      if type(elem) == int:
        myset.add(elem)

    outlist = list(myset)
    outlist.sort()

    print('Sorted unique list=')
    print(outlist)

if __name__ == '__main__':
    print('module only, not main')