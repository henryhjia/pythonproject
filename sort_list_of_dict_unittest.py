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

  def tearDown(self):
    print('teardown')          

  def test_1_sort_list_of_dictionary_by_value(self) -> None:
    my_list_of_dict = [
      {'name':'Sam', 'number': 11}, 
      {'name':'Jan', 'number': 1},
      {'name':'Kate', 'number':9},
      {'name':'Bob', 'number':13}
    ]
    result = self.me.sort_list_of_dictionary_by_value(my_list_of_dict)
    
    self.assertEqual(result[0]['number'], 1)
    self.assertEqual(result[1]['number'], 9)
    self.assertEqual(result[2]['number'], 11)
    self.assertEqual(result[3]['number'], 13)            

  def test_2_sort_list_of_dictionary_by_key(self) -> None:
    my_list_of_dict = [
      {'name':'Sam', 'number': 11}, 
      {'name':'Jan', 'number': 1},
      {'name':'Kate', 'number':9},
      {'name':'Bob', 'number':13}
    ]
    result = self.me.sort_list_of_dictionary_by_key(my_list_of_dict)

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

if __name__ == '__main__':
  unittest.main()
