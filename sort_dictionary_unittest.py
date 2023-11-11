"""
sort dictionary unittest
@sortdictionary unittest

usage: python3 -m unittest sort_dictionary_unittest.UnitTest -v

"""
import unittest
# following is for retrieving a module from PyPI library hjlibrary
# from hjlibrary.dictionary_sort_module import SortDictionaryModule
import dictionary_sort_module

class UnitTest(unittest.TestCase):
  def setUp(self):
    print('setup')
    self.me = dictionary_sort_module.SortDictionaryModule()
    # Following statement is for using PyPI library hjlibrary
    # self.me = SortDictionaryModule()
    self.in_dict = { 
        'Sam': 12, 
        'Bob': 1, 
        'Kate': 8, 
        'Jan': 13
      }
    
    self.test_str2 = '{"eggs":1, "coffee":9.99, "rice":4.04}'

  def tearDown(self):
    print('teardown')

  def test_1_sort_dictionary_by_value(self):

    result = self.me.sort_dictionary_by_value(self.in_dict)

    value_list = list(result.values())
    self.assertEqual(value_list[0], 1)
    self.assertEqual(value_list[1], 8)
    self.assertEqual(value_list[2], 12)
    self.assertEqual(value_list[3], 13)

  def test_2_sort_dictionary_by_key(self):

    result = self.me.sort_dictionary_by_key(self.in_dict)

    key_list = list(result.keys())
    self.assertEqual(key_list[0], 'Bob')
    self.assertEqual(key_list[1], 'Jan')
    self.assertEqual(key_list[2], 'Kate')
    self.assertEqual(key_list[3], 'Sam')

  def test_3_sort_by_price_ascending_by_key(self) -> None:
    result = self.me.sort_by_price_ascending_by_key(self.test_str2)
    result_keys = list(result.keys())
    self.assertEqual(result_keys[0], 'coffee')
    self.assertEqual(result_keys[1], 'eggs')
    self.assertEqual(result_keys[2], 'rice')        

  def test_4_sort_by_price_ascending_by_value(self) -> None:
    result = self.me.sort_by_price_ascending_by_value(self.test_str2)
    result_values = list(result.values())    
    self.assertEqual(result_values[0], 1)
    self.assertEqual(result_values[1], 4.04)
    self.assertEqual(result_values[2], 9.99)     

  def test_5_sort_by_price_descending_by_key(self) -> None:
    result = self.me.sort_by_price_descending_by_key(self.test_str2)
    result_keys = list(result.keys())
    self.assertEqual(result_keys[0], 'rice')
    self.assertEqual(result_keys[1], 'eggs')
    self.assertEqual(result_keys[2], 'coffee')    

  def test_6_sort_by_price_descending_by_value(self) -> None:
    result = self.me.sort_by_price_descending_by_value(self.test_str2)
    result_values = list(result.values())    
    self.assertEqual(result_values[0], 9.99)
    self.assertEqual(result_values[1], 4.04)
    self.assertEqual(result_values[2], 1)    

if __name__ == '__main__':
  unittest.main()
