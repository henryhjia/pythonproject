"""
Sort list module
@sortlist

@brief  This module provides sort of list and sort of list of dictionaries methods

Two methods for sorting a list:
  1. l2 = sorted(l1) - create a new list that is sorted
  2. l1.sort() - in place sort

Two methods for soritng list of dictionary:
  1. Sort list of dictionaries
     a. sort the list of dictionaires by using sorted(list_of_dict, key=lambda, x:x[''] notation)
  2. Sort list of complex dictionary
"""
import json
import ast
import common_module

class ListSortModule:
  """
  @brief This module provides various sorting list methods
  """
  def __init__(self):
    """
    """
    pass

  def sort_sorted(self, l1:list) -> list:
    """
    @brief use Python build-in sorted() to sort a list
    @param l1: input list
    @return l2: sorted list
    """
    common_module.print_function(self.sort_sorted)
    l2 = sorted(l1)
    return l2
  
  def sort_in_place_sort(self, l1: list) -> list:
    """
    @brief use Python build-in in-place sort()
    @param l1: input list
    @return sorted list
    """
    common_module.print_function(self.sort_in_place_sort)
    l1.sort()

    return l1
  
  def sort_integer_unique_mixed_data_type_in_list(self, mylist: list) -> list:
    """
    @brief Given a list of different type, sort the integers in the list in asend order, 
    no duplicate
    Since it requires unique, a set is used
    @param mulist: input list
    @return a sorted list
    """
    common_module.print_function(self.sort_integer_unique_mixed_data_type_in_list)

    myset = set()

    for elem in mylist:
      if type(elem) == int:
        myset.add(elem)

    outlist = list(myset)
    outlist.sort()

    return outlist

  def sort_list_of_dictionary_by_value(self, in_list_dict: list, value_name: str) -> list:
    """
    @brief sort list of dictionary by value
    @param in_list_dict: input list of dictionary
    @param value_name: name of the value to sort upon
    @return sorted list of dictionary (by value)
    """
    common_module.print_function(self.sort_list_of_dictionary_by_value)
    sorted_list_of_dictionary = sorted(in_list_dict, key=lambda x:x[value_name])
    return sorted_list_of_dictionary
  
  def sort_list_of_dictionary_by_key(self, in_list_dict: list, key_name:str) -> list:
    """
    @brief sort list of dictionary by key
    @param in_list_dict: input list of dictionary
    @param key_name: name of the key to sort upon
    @return sorted list of dictionary (by key)    
    """
    common_module.print_function(self.sort_list_of_dictionary_by_key)
    sorted_list_of_dictionary = sorted(in_list_dict, key=lambda x:x[key_name])
    return sorted_list_of_dictionary

  def sort_list_of_complex_dictionary(self, my_list_of_dict: list, index: int) -> list:
    """
    @brief sort the list of dictionary, the value of the dictionary is a list, sort the 
           dictionary by the index of the list
    @param list: list of dictionary
    @param index: index of the list, the index is used to sort
    """
    common_module.print_function(self.sort_list_of_complex_dictionary)       
    sorted_list = sorted(my_list_of_dict, key=lambda x:x[list(x.keys())[0]][index])     
    return sorted_list
  
  def sort_list_of_list(self, my_list, index: int) -> list:
    """
    @brief Sort list of list
    @param my_list: list of list
    @param index: sort the list base on the index of the innner list
    @return sorted list
    """
    common_module.print_function(self.sort_list_of_list) 
    sorted_list = sorted(my_list, key=lambda x:x[index])
    return sorted_list

  def sort_by_price_ascending_by_price_ast_literal_eval(self, json_string: str, key_name: str) -> list:
    """
    @brief convert to a list of dictionaries from a string json_string
    @param json_string: str
    @param key_name: str, name of the key to sort uopn
    @return sorted_list: list
    """
    list_of_dictionaries = ast.literal_eval(json_string)

    # sort the list of dictionaires by key_name in the dictionary
    sorted_list = sorted(list_of_dictionaries, key=lambda x:x[key_name])

    return sorted_list

  def sort_by_price_ascending_by_price_json_loads(self, json_string: str, key_name: str) -> list:
    """
    @brief convert to a list of dictionaries from a string json_string
    @param json_string: str
    @param key_name: str, name of the key to sort uopn
    @return sorted_list: list  
    """
    list_of_dictionaries = json.loads(json_string)

    # sort the list of dictionaires by key_name in the dictionary
    sorted_list = sorted(list_of_dictionaries, key=lambda x:x[key_name])

    return sorted_list

  def sort_by_price_ascending_by_name_ast_literal_eval(self, json_string: str, key_name: str) -> list:
    """
    @brief convert to a list of dictionaries from a string json_string
    @param json_string: str
    @param key_name: str, name of the key to sort uopn
    @return sorted_list: list
    """
    list_of_dictionaries = ast.literal_eval(json_string)

    # sort the list of dictionaires by key_name in the dictionary
    sorted_list = sorted(list_of_dictionaries, key=lambda x:x[key_name])

    return sorted_list

  def sort_by_price_ascending_by_name_json_loads(self, json_string: str, key_name: str) -> list:
    """
    @brief convert to a list of dictionaries from a string json_string
    @param json_string: str
    @param key_name: str, name of the key to sort uopn    
    @return sorted_list: list
    """
    list_of_dictionaries = json.loads(json_string)

    # sort the list of dictionaires by key_name in the dictionary
    sorted_list = sorted(list_of_dictionaries, key=lambda x:x[key_name])

    return sorted_list

  def sort_by_price_descending_by_name(self, json_string: str, key_name: str) -> list:
    """
    @brief convert to a list of dictionaries from a string json_string
    @param json_string: str
    @param key_name: str, name of the key to sort uopn     
    @return sorted_list: list
    """
    list_of_dictionaries = json.loads(json_string)

    # sort the list of dictionaires by key_name in the dictionary
    sorted_list = sorted(list_of_dictionaries, key=lambda x:x[key_name], reverse=True)

    return sorted_list

  def sort_by_price_descending_by_price(self, json_string: str, key_name: str) -> list:
    """
    @brief convert to a list of dictionaries from a string json_string
    @param json_string: str
    @return sorted_list: list        
    """
    list_of_dictionaries = json.loads(json_string)

    # sort the list of dictionaires by key_name in the dictionary
    sorted_list = sorted(list_of_dictionaries, key=lambda x:x[key_name], reverse=True)

    return sorted_list


if __name__ == '__main__':
    print('module only, not main')