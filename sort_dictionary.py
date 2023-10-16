#!/use/bin/python3
"""
Sort dictionary
@sortdictionary

"""
import dictionary_sort_module

def main() -> None:

  me = dictionary_sort_module.SortDictionaryModule()

  # Sort dictionary by value
  in_dict = { 
      'Sam': 12, 
      'Bob': 1, 
      'Kate': 8, 
      'Jan': 13
    }
  print(in_dict)
  result = me.sort_dictionary_by_value(in_dict)
  print(result)

  # Sort dictionary by key
  result = me.sort_dictionary_by_key(in_dict)
  print(result)

if __name__ == '__main__':
  main()