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
  
if __name__ == '__main__':
    print('module only, not main')