"""
Sort list
@sortlist

Two methods:
l2 = sorted(l1) - create a new list that is sorted
l1.sort() - in place sort

"""
import json
import ast
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

  def sort_list_of_list(self) -> None:
    """
    1. Sort list of list
    """
    common_module.print_function(self.sort_list_of_list) 
    
    my_list = [
      [1,2,3],
      [3,2,1],
      [2,5,5],
      [0,1,4]
    ]

    for i in my_list:
      print(i)

    sorted_list = sorted(my_list, key=lambda x:x[0])
    print('sort based on x[0]')
    for i in sorted_list:
      print(i)

    sorted_list = sorted(my_list, key=lambda x:x[1])
    print('sort based on x[1]')
    for i in sorted_list:
      print(i)

    sorted_list = sorted(my_list, key=lambda x:x[2])
    print('sort based on x[2]')
    for i in sorted_list:
      print(i)

  def sort_by_price_ascending_by_price_ast_literal_eval(self, json_string):
      # convert to a list of dictionaries from a string json_string
      # method 1:
      list_of_dictionaries = ast.literal_eval(json_string)

      # sort the list of dictionaires by the value 'price' in the dictionary
      sorted_list = sorted(list_of_dictionaries, key=lambda x:x['price'])

      return sorted_list

  def sort_by_price_ascending_by_price_json_loads(self, json_string):
      # convert to a list of dictionaries from a string json_string
      # method 2:
      list_of_dictionaries = json.loads(json_string)

      # sort the list of dictionaires by the value 'price' in the dictionary
      sorted_list = sorted(list_of_dictionaries, key=lambda x:x['price'])

      return sorted_list

  def sort_by_price_ascending_by_name_ast_literal_eval(self, json_string):
      # convert to a list of dictionaries from a string json_string
      # method 1:
      list_of_dictionaries = ast.literal_eval(json_string)

      # sort the list of dictionaires by the value 'price' in the dictionary
      sorted_list = sorted(list_of_dictionaries, key=lambda x:x['name'])

      return sorted_list

  def sort_by_price_ascending_by_name_json_loads(self, json_string):
      # convert to a list of dictionaries from a string json_string
      # method 2:
      list_of_dictionaries = json.loads(json_string)

      # sort the list of dictionaires by the value 'price' in the dictionary
      sorted_list = sorted(list_of_dictionaries, key=lambda x:x['name'])

      return sorted_list

  def sort_by_price_descending_by_name(self, json_string):
      # convert to a list of dictionaries from a string json_string
      # method 2:
      list_of_dictionaries = json.loads(json_string)

      # sort the list of dictionaires by the value 'price' in the dictionary
      sorted_list = sorted(list_of_dictionaries, key=lambda x:x['name'], reverse=True)

      return sorted_list

  def sort_by_price_descending_by_price(self, json_string):
      # convert to a list of dictionaries from a string json_string
      # method 2:
      list_of_dictionaries = json.loads(json_string)

      # sort the list of dictionaires by the value 'price' in the dictionary
      sorted_list = sorted(list_of_dictionaries, key=lambda x:x['price'], reverse=True)

      return sorted_list

  def sort_by_price_ascending_by_key(self, json_string):
      # convert to a dictionaries from a string json_string, then sort dictionary by key

      mydic = json.loads(json_string)
      mysorted_list = sorted(mydic.items())
      sorted_dict = dict(mysorted_list)

      return sorted_dict

  def sort_by_price_ascending_by_value(self, json_string):
      # convert to a dictionaries from a string json_string, then sort dictionary by value

      mydic = json.loads(json_string)
      mysorted_list = sorted(mydic.items(), key=lambda x:x[1])
      sorted_dict = dict(mysorted_list)

      return sorted_dict

  def sort_by_price_descending_by_key(self, json_string):
      # convert to a dictionaries from a string json_string, then sort dictionary by value

      mydic = json.loads(json_string)
      mysorted_list = sorted(mydic.items(), reverse=True)
      sorted_dict = dict(mysorted_list)

      return sorted_dict

  def sort_by_price_descending_by_value(self, json_string):
      # convert to a dictionaries from a string json_string, then sort dictionary by value

      mydic = json.loads(json_string)
      mysorted_list = sorted(mydic.items(), key=lambda x:x[1], reverse=True)
      sorted_dict = dict(mysorted_list)

      return sorted_dict

if __name__ == '__main__':
    print('module only, not main')