"""
slice string unittest
@slicestring unittest

usage: python3 -m unittest slice_string_unittest.UnitTest -v

"""
import unittest
import string_slicing_module

class UnitTest(unittest.TestCase):

  def test_1_reverse_data_using_slicing(self):

    me = string_slicing_module.StringSlicingTester()

    # find a string
    in_str = 'ABCCDCDCDCDC'
    pattern = 'CDC'
    result = me.find_string_by_coding(in_str, pattern)
    self.assertEqual(result, 4)

  def test_2_reverse_data_manually(self):
    me = string_slicing_module.StringSlicingTester()

    # find a string
    in_str = 'ABCCDCDCDCDC'
    pattern = 'CDC'

    result = me.find_string_using_slicing(in_str, pattern)
    self.assertEqual(result, 4)

if __name__ == '__main__':
  unittest.main()
