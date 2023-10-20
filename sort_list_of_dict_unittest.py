"""
sort list unittest
@sortlist unittest

usage: python3 -m unittest sort_list_of_dict_unittest.UnitTest -v

"""
import unittest
import list_sort_module

class UnitTest(unittest.TestCase):
  def setUp(self):
    print('setup')
    self.me = list_sort_module.SortListModule()
    self.my_list_of_dict = [
      {'name':'Sam', 'number': 11}, 
      {'name':'Jan', 'number': 1},
      {'name':'Kate', 'number':9},
      {'name':'Bob', 'number':13}
    ]    

    self.test_str = '[{"name":"eggs","price":1},{"name":"coffee","price":9.99},{"name":"rice","price":4.04}]'
    self.test_str2 = '{"eggs":1, "coffee":9.99, "rice":4.04}'

  def tearDown(self):
    print('teardown')          

  def test_1_sort_list_of_dictionary_by_value(self) -> None:
    result = self.me.sort_list_of_dictionary_by_value(self.my_list_of_dict)
    
    self.assertEqual(result[0]['number'], 1)
    self.assertEqual(result[1]['number'], 9)
    self.assertEqual(result[2]['number'], 11)
    self.assertEqual(result[3]['number'], 13)            

  def test_2_sort_list_of_dictionary_by_key(self) -> None:
    result = self.me.sort_list_of_dictionary_by_key(self.my_list_of_dict)

    self.assertEqual(result[0]['name'], 'Bob')
    self.assertEqual(result[1]['name'], 'Jan')
    self.assertEqual(result[2]['name'], 'Kate')
    self.assertEqual(result[3]['name'], 'Sam')   

  def test_3_sort_list_of_complex_dictionary(self) -> None:
    my_list_of_dict = [
        { "dad": ["Ted",32,72]},
        { "mom": ["Karren",2,68]},
        { "daughter": ["Sue",9,42]},
        { "daughter": ["Linda",11,38]}
    ]
    result = self.me.sort_list_of_complex_dictionary(my_list_of_dict, 0)

    self.assertEqual(result[0]['mom'][0], 'Karren')
    self.assertEqual(result[1]['daughter'][0], 'Linda')
    self.assertEqual(result[2]['daughter'][0], 'Sue')
    self.assertEqual(result[3]['dad'][0], 'Ted')

    result = self.me.sort_list_of_complex_dictionary(my_list_of_dict, 1)

    self.assertEqual(result[0]['mom'][1], 2)
    self.assertEqual(result[1]['daughter'][1], 9)
    self.assertEqual(result[2]['daughter'][1], 11)
    self.assertEqual(result[3]['dad'][1], 32)

    result = self.me.sort_list_of_complex_dictionary(my_list_of_dict, 2)

    self.assertEqual(result[0]['daughter'][2], 38)
    self.assertEqual(result[1]['daughter'][2], 42)
    self.assertEqual(result[2]['mom'][2], 68)
    self.assertEqual(result[3]['dad'][2], 72)

  def test_4_sort_by_price_ascending_by_price_ast_literal_eval(self) -> None:
    result = self.me.sort_by_price_ascending_by_price_ast_literal_eval(self.test_str)
    self.assertEqual(result[0]['price'], 1)
    self.assertEqual(result[1]['price'], 4.04)
    self.assertEqual(result[2]['price'], 9.99)

  def test_5_sort_by_price_ascending_by_price_json_loads(self) -> None:
    result = self.me.sort_by_price_ascending_by_price_json_loads(self.test_str)
    self.assertEqual(result[0]['price'], 1)
    self.assertEqual(result[1]['price'], 4.04)
    self.assertEqual(result[2]['price'], 9.99)    

  def test_6_sort_by_price_ascending_by_name_ast_literal_eval(self) -> None:
    result = self.me.sort_by_price_ascending_by_name_ast_literal_eval(self.test_str)
    self.assertEqual(result[0]['name'], 'coffee')
    self.assertEqual(result[1]['name'], 'eggs')
    self.assertEqual(result[2]['name'], 'rice')  

  def test_7_sort_by_price_ascending_by_name_json_loads(self) -> None:
    result = self.me.sort_by_price_ascending_by_name_json_loads(self.test_str)
    self.assertEqual(result[0]['name'], 'coffee')
    self.assertEqual(result[1]['name'], 'eggs')
    self.assertEqual(result[2]['name'], 'rice') 

  def test_8_sort_by_price_descending_by_name(self) -> None:
    result = self.me.sort_by_price_descending_by_name(self.test_str)
    self.assertEqual(result[0]['name'], 'rice')
    self.assertEqual(result[1]['name'], 'eggs')
    self.assertEqual(result[2]['name'], 'coffee') 

  def test_9_sort_by_price_descending_by_price(self) -> None:
    result = self.me.sort_by_price_descending_by_price(self.test_str)
    self.assertEqual(result[0]['price'], 9.99)
    self.assertEqual(result[1]['price'], 4.04)
    self.assertEqual(result[2]['price'], 1)  

  def test_10_sort_by_price_ascending_by_key(self) -> None:
    result = self.me.sort_by_price_ascending_by_key(self.test_str2)
    result_keys = list(result.keys())
    self.assertEqual(result_keys[0], 'coffee')
    self.assertEqual(result_keys[1], 'eggs')
    self.assertEqual(result_keys[2], 'rice')        

  def test_11_sort_by_price_ascending_by_value(self) -> None:
    result = self.me.sort_by_price_ascending_by_value(self.test_str2)
    result_values = list(result.values())    
    self.assertEqual(result_values[0], 1)
    self.assertEqual(result_values[1], 4.04)
    self.assertEqual(result_values[2], 9.99)     

  def test_12_sort_by_price_descending_by_key(self) -> None:
    result = self.me.sort_by_price_descending_by_key(self.test_str2)
    result_keys = list(result.keys())
    self.assertEqual(result_keys[0], 'rice')
    self.assertEqual(result_keys[1], 'eggs')
    self.assertEqual(result_keys[2], 'coffee')    

  def test_13_sort_by_price_descending_by_value(self) -> None:
    result = self.me.sort_by_price_descending_by_value(self.test_str2)
    result_values = list(result.values())    
    self.assertEqual(result_values[0], 9.99)
    self.assertEqual(result_values[1], 4.04)
    self.assertEqual(result_values[2], 1)     


if __name__ == '__main__':
  unittest.main()
