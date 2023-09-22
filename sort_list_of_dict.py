#!/use/bin/python3
"""
Sort list of dictionary
@sortlistofdictionary
list and dictionary are populated in the program
"""
import list_sort_module

def main() -> int:

  me = list_sort_module.SortListTester()

  me.sort_list_of_dictionary_by_value()
  me.sort_list_of_dictionary_by_key()
  me.sort_list_of_complex_dictionary()

if __name__ == '__main__':
  main()