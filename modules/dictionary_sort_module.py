#!/use/bin/python3
"""
dictionary sort
@sortdictionary

methods for sorting a dictionary
"""
import common_module

class SortDictionaryTester:
  """
  """
  def __init__(self):
    pass
  
  def sort_dictionary_by_value(self):
    """
    """
    common_module.print_function(self.sort_dictionary_by_value)
    my_dict = { 
        'Sam': 12, 
        'Bob': 1, 
        'Kate': 8, 
        'Jan': 13
      }
    print('my_dict=', my_dict)
    mylist = sorted(my_dict.items(), key=lambda x:x[1])
    print('sorted list view=', mylist)
    sorted_dict = dict(mylist)
    print('sorted_dict by value=', sorted_dict)

  def sort_dictionary_by_key(self):
    common_module.print_function(self.sort_dictionary_by_key)
    my_dict = { 
        'Sam': 12, 
        'Bob': 1, 
        'Kate': 8, 
        'Jan': 13
      }
    # The next two methods are the same, the second one uses default  
    # mylist = sorted(my_dict.items(), key=lambda x:x[0])
    # mylist = sorted(my_dict.items())
    print('my_dict=', my_dict)
    mylist = sorted(my_dict.items())
    print('sorted list view=', mylist)
    sorted_dict = dict(mylist)
    print('sorted_dict by key=', sorted_dict)

if __name__ == '__main__':
    print('module only, not main')