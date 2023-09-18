#!/use/bin/python3
"""
Python practice
Count number of occurrence of appearence of a value in the dictionary
"""

class DictionaryItemTester:
  """
  @brief
  """

  def __init__(self) -> None:
    """
    @brief constructor
    """
    pass

  
  def get_list_with_2nd_min_value_in_dictionary(self, in_dict) -> list:
    ""
    print('\n*********** get_list_with_2nd_min_value_in_dictionary()')
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

  
def main() -> int:
  """
  """

  me = DictionaryItemTester()

  # get a new list with each item's value is the second minimum in the original dictionary
  my_dict = { 'henry': 40, 'jean': 30, 'claire': 30, 'maggie': 10}
  new_list = me.get_list_with_2nd_min_value_in_dictionary(my_dict)
  print('new list=', new_list)

if __name__ == '__main__':
  main()
