"""
slice string unittest
@slicestring unittest

Usage: python3 -m unittest slice_string_unittest.UnitTest -v
Usage: in pythonproj/ run python -m basics.slice_string_unittest

"""
import unittest
from modules import string_slicing_module

class UnitTest(unittest.TestCase):
  def setUp(self):
    print('setup')
    self.me = string_slicing_module.StringSlicingModule()

  def tearDown(self):
    print('teardown')

  def test_1_reverse_data_using_slicing(self):

    # find a string
    in_str = 'ABCCDCDCDCDC'
    pattern = 'CDC'
    result = self.me.find_string_using_looping(in_str, pattern)
    self.assertEqual(result, 4)

  def test_2_reverse_data_manually(self):

    # find a string
    in_str = 'ABCCDCDCDCDC'
    pattern = 'CDC'

    result = self.me.find_string_using_slicing(in_str, pattern)
    self.assertEqual(result, 4)

if __name__ == '__main__':
  unittest.main()
