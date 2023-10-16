"""
slice string unittest
@slicestring unittest

usage: python3 -m unittest sort_dictionary_unittest.UnitTest -v

"""
import unittest
import dictionary_sort_module

class UnitTest(unittest.TestCase):
  def setUp(self):
    print('setup')
    self.me = dictionary_sort_module.SortDictionaryModule()

  def tearDown(self):
    print('teardown')

  def test_1_sort_dictionary_by_value(self):
    in_dict = { 
        'Sam': 12, 
        'Bob': 1, 
        'Kate': 8, 
        'Jan': 13
      }
    print(in_dict)
    result = self.me.sort_dictionary_by_value(in_dict)

    value_list = list(result.values())
    self.assertEqual(value_list[0], 1)
    self.assertEqual(value_list[1], 8)
    self.assertEqual(value_list[2], 12)
    self.assertEqual(value_list[3], 13)

  def test_2_sort_dictionary_by_key(self):
    in_dict = { 
        'Sam': 12, 
        'Bob': 1, 
        'Kate': 8, 
        'Jan': 13
      }    
    result = self.me.sort_dictionary_by_key(in_dict)

    key_list = list(result.keys())
    self.assertEqual(key_list[0], 'Bob')
    self.assertEqual(key_list[1], 'Jan')
    self.assertEqual(key_list[2], 'Kate')
    self.assertEqual(key_list[3], 'Sam')


if __name__ == '__main__':
  unittest.main()
