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
  def __init__(self):
    """
    """
    self._my_list_of_dict = [
        {'name':'Sam', 'number': 11}, 
        {'name':'Jan', 'number': 1},
        {'name':'Kate', 'number':9},
        {'name':'Bob', 'number':13}
    ]

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

  def sort_list_of_dictionary_by_value(self) -> None:
    """
    1. Sort a dictionary
       a. sort dic.items() so it becomes a list of tuples
       b. convert the list of tuple to a dictionary
    2. Sort list of dictionaries
       a. sort the list of dictionaires by using sort(list_of_dict, key=lambda, x:x[''] notation)
    3. Sort list of complex dictionary
    """
    common_module.print_function(self.sort_list_of_dictionary_by_value)
  
    my_list_of_dict = [
        {'name':'Sam', 'number': 11}, 
        {'name':'Jan', 'number': 1},
        {'name':'Kate', 'number':9},
        {'name':'Bob', 'number':13}
    ]
    print('my_list_of_dict=', self._my_list_of_dict)
    sorted_list_of_dictionary = sorted(self._my_list_of_dict, key=lambda x:x['number'])
    print('sorted list of dictionary=', sorted_list_of_dictionary)

  def sort_list_of_dictionary_by_key(self) -> None:
    common_module.print_function(self.sort_list_of_dictionary_by_key)
  
    print('my_list_of_dict=', self._my_list_of_dict)
    sorted_list_of_dictionary = sorted(self._my_list_of_dict, key=lambda x:x['name'])
    print('sorted list of dictionary=', sorted_list_of_dictionary)

  def sort_list_of_complex_dictionary(self) -> None:
    common_module.print_function(self.sort_list_of_complex_dictionary)

    my_list_of_dict = [
        { "dad": ["Ted",32,72]},
        { "mom": ["Karren",2,68]},
        { "daughter": ["Sue",9,42]},
        { "daughter": ["Linda",11,38]}
    ]
    print('my_list_of_dict=', my_list_of_dict)

    sorted_list = sorted(my_list_of_dict, key=lambda x:x[list(x.keys())[0]][1])     
    print('sort by value 1:', sorted_list)

    sorted_list = sorted(my_list_of_dict, key=lambda x:x[list(x.keys())[0]][2])     
    print('sort by value 2:', sorted_list)

    sorted_list = sorted(my_list_of_dict, key=lambda x:x[list(x.keys())[0]][0])     
    print('sort by value 0:', sorted_list)

    sorted_list = sorted(my_list_of_dict, key=lambda d: list(d.keys())[0])     
    print('sort by key:    ', sorted_list)

if __name__ == '__main__':
    print('module only, not main')