"""
count occurence from a dictionary unittest
@countoccurence unittest

usage: python3 -m unittest count_occur_from_dict_unittest.UnitTest -v

"""
import unittest
import dictionary_process_module

class UnitTest(unittest.TestCase):
  def setUp(self):
    print('setup')
    self.me = dictionary_process_module.ProcessDictionaryModule()

  def tearDown(self):
    print('teardown')          

  def test_1_get_list_with_2nd_min_value_in_dictionary(self) -> None:
    my_dict = { 'David': 40, 'Mark': 30, 'Jean': 30, 'Kate': 10}
    result = self.me.get_list_with_2nd_min_value_in_dictionary(my_dict)
    print(result)
    self.assertEqual(result[0], 'Mark')
    self.assertEqual(result[1], 'Jean')    
    
if __name__ == '__main__':
  unittest.main()
