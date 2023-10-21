"""
sort string unittest
@sortstring unittest

usage: python3 -m unittest sort_string_unittest.UnitTest -v

"""
import unittest
import string_sort_module

class UnitTest(unittest.TestCase):
  def setUp(self):
    print('setup')
    self.me = string_sort_module.StringSortModule()
    self.data = "google"

  def tearDown(self):
    print('teardown')

  def test_1_sort_string_data(self):

    # sort string
    result = self.me.sort_string_data(self.data)
    self.assertEqual(result[0], 'e')
    self.assertEqual(result[1], 'g')
    self.assertEqual(result[2], 'g')
    self.assertEqual(result[3], 'l')
    self.assertEqual(result[4], 'o')
    self.assertEqual(result[5], 'o')
                 

  def test_2_sort_sort_alpha_digit(self):
    in_string = "Sorted1234"
    result = self.me.sort_alpha_digit(in_string)

    self.assertEqual(result[0], 'd')
    self.assertEqual(result[1], 'e')
    self.assertEqual(result[2], 'o')
    self.assertEqual(result[3], 'r')
    self.assertEqual(result[4], 't')
    self.assertEqual(result[5], 'S')
    self.assertEqual(result[6], '1')
    self.assertEqual(result[7], '3')
    self.assertEqual(result[8], '2')
    self.assertEqual(result[9], '4')                
                 

if __name__ == '__main__':
  unittest.main()
