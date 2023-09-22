#!/use/bin/python3
"""
Python practice
Count number of occurrence of appearence of a value in the dictionary
"""
import dictionary_process_module
  
def main() -> int:
  """
  """

  me = dictionary_process_module.ProcessDictionary()

  # get a new list with each item's value is the second minimum in the original dictionary
  my_dict = { 'David': 40, 'Mark': 30, 'Jean': 30, 'Kate': 10}
  new_list = me.get_list_with_2nd_min_value_in_dictionary(my_dict)
  print('new list=', new_list)

if __name__ == '__main__':
  main()
