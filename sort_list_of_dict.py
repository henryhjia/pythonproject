"""
Sort list of dictionary
@sortlistofdictionary
list and dictionary are populated in the program
"""
import list_sort_module

def main() -> None:

  me = list_sort_module.ListSortModule()

  # sort list of dictionary
  my_list_of_dict = [
    {'name':'Sam', 'number': 11}, 
    {'name':'Jan', 'number': 1},
    {'name':'Kate', 'number':9},
    {'name':'Bob', 'number':13}
  ]
  print(my_list_of_dict)
  result = me.sort_list_of_dictionary_by_value(my_list_of_dict)
  print(result)

  result = me.sort_list_of_dictionary_by_key(my_list_of_dict)
  print(result)

  my_list_of_dict = [
      { "dad": ["Ted",32,72]},
      { "mom": ["Karren",2,68]},
      { "daughter": ["Sue",9,42]},
      { "daughter": ["Linda",11,38]}
  ]

  result = me.sort_list_of_complex_dictionary(my_list_of_dict, 0)
  print('sot by list index 0')
  print(my_list_of_dict)
  print(result)

  result = me.sort_list_of_complex_dictionary(my_list_of_dict, 1)
  print('sot by list index 1')
  print(my_list_of_dict)
  print(result)

  result = me.sort_list_of_complex_dictionary(my_list_of_dict, 2)
  print('sot by list index 2')  
  print(my_list_of_dict)
  print(result)


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