#!/use/bin/python3
"""
Sort dictionary
@sortdictionary

"""
from modules import dictionary_sort_module

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


  order = 1
  # for string data '{"eggs":1, "coffee":9.99, "rice":4.04}'
  str2 = '{"eggs":1, "coffee":9.99, "rice":4.04}'
  # use class method (static method)
  print(f'{order: 3d}', dictionary_sort_module.SortDictionaryModule.sort_by_price_ascending_by_key(str2))
  order += 1

  print(f'{order: 3d}', dictionary_sort_module.SortDictionaryModule.sort_by_price_ascending_by_value(str2))
  order += 1

  print(f'{order: 3d}', dictionary_sort_module.SortDictionaryModule.sort_by_price_descending_by_key(str2))
  order += 1

  # you can aso use instance to call a static method
  print(f'{order: 3d}', dictionary_sort_module.SortDictionaryModule.sort_by_price_descending_by_value(str2))
if __name__ == '__main__':
  main()