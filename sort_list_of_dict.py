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

  # sort list of dictionaries, the list data is populated using json.loads() or ast.literal_eval() 
  # from string representation of a list of dictionary
  #
  # two print formats:
  # 1. format: print(format(order, '3d'))
  # 2. f notation: print(f'{order: 3d}')
  #

  order = 1
  # for string data ''[{"name":"eggs","price":1},{"name":"coffee","price":9.99},{"name":"rice","price":4.04}]')'
  str1 = '[{"name":"eggs","price":1},{"name":"coffee","price":9.99},{"name":"rice","price":4.04}]'
  print(format(order, '3d'), me.sort_by_price_ascending_by_price_ast_literal_eval(str1))
  order += 1

  print(format(order, '3d'), me.sort_by_price_ascending_by_price_json_loads(str1))
  order += 1

  print(f'{order: 3d}', me.sort_by_price_ascending_by_name_ast_literal_eval(str1))
  order += 1

  print(f'{order: 3d}', me.sort_by_price_ascending_by_name_json_loads(str1))
  order += 1

  print(f'{order: 3d}', me.sort_by_price_descending_by_name(str1))
  order += 1

  print(f'{order: 3d}', me.sort_by_price_descending_by_price(str1))
  order += 1

  # for string data '{"eggs":1, "coffee":9.99, "rice":4.04}'
  str2 = '{"eggs":1, "coffee":9.99, "rice":4.04}'
  print(f'{order: 3d}', me.sort_by_price_ascending_by_key(str2))
  order += 1

  print(f'{order: 3d}', me.sort_by_price_ascending_by_value(str2))
  order += 1

  print(f'{order: 3d}', me.sort_by_price_descending_by_key(str2))
  order += 1

  print(f'{order: 3d}', me.sort_by_price_descending_by_value(str2))

if __name__ == '__main__':
  main()