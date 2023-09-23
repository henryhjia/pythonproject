#!/use/bin/python3
"""
process list
@processlist

methods for processing a list
"""
import common_module

class ProcessList:
  """
  """
  def __init__(self):
    pass
  
  def get_list_with_2nd_min_value_in_dictionary(self, in_dict) -> list:
    ""
    common_module.print_function(self.get_list_with_2nd_min_value_in_dictionary)

    print('input dict=', in_dict)

    value_list = list(in_dict.values())
    value_list.sort()
    print('sorted values=', value_list)    
    min = value_list[0]
    second_min = 0
    for i in value_list:
      if i > min:
        second_min = i
        break

    print(f'second minimum value = {second_min}')

    new_list = []
    for key, value in in_dict.items():
      print(key, value)
      if value == second_min:
        new_list.append(key)

    return new_list
  
  def reverse_list_by_coding(self, in_list: list) -> list:
    """
    """
    common_module.print_function(self.reverse_list_by_coding)

    out_list = []
    list_size = len(in_list)

    for i in range(list_size-1, -1, -1):
      out_list.append(in_list[i])

    return out_list

  def reverse_list_using_slicing(self, in_list: list) -> list:
    """
    A copy of a reversed list is generated
    """
    common_module.print_function(self.reverse_list_using_slicing)
    out_list = in_list[::-1]

    return out_list
  
if __name__ == '__main__':
    print('module only, not main')