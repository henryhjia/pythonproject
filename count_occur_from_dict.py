"""
Python practice
Count number of occurrence of appearence of a value in the dictionary
"""
import dictionary_process_module
  
def main() -> None:
  """
  """

  me = dictionary_process_module.ProcessDictionaryModule()

  # get a new list with each item's value is the second minimum in the original dictionary
  my_dict = { 'David': 40, 'Mark': 30, 'Jean': 30, 'Kate': 10}
  print('original dict=', my_dict)
  new_list = me.get_list_with_2nd_min_value_in_dictionary(my_dict)
  print('list with second min=', new_list)

if __name__ == '__main__':
  main()
