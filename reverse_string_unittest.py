"""
Reverse string unittest
@reversestring unittest

usage: python3 -m unittest reverse_string_unittest.UnitTest -v

  me.reverse_data_using_slicing(args[1])
  me.reverse_data_manually(args[1])

"""
import unittest
import string_reverse_module

class UnitTest(unittest.TestCase):

  def test_1_reverse_data_using_slicing(self):
    me = string_reverse_module.ReverseStringTester()
    orig_string = "google"
    reversed_string = me.reverse_data_using_slicing(orig_string)

    self.assertEqual(reversed_string[0], orig_string[5])
    self.assertEqual(reversed_string[1], orig_string[4])
    self.assertEqual(reversed_string[2], orig_string[3])
    self.assertEqual(reversed_string[3], orig_string[2])            
    self.assertEqual(reversed_string[4], orig_string[1])    
    self.assertEqual(reversed_string[5], orig_string[0])    

  def test_2_reverse_data_manually(self):
    me = string_reverse_module.ReverseStringTester()

    orig_string = "amazon"    
    reversed_string = me.reverse_data_manually(orig_string)

    self.assertEqual(reversed_string[0], orig_string[5])
    self.assertEqual(reversed_string[1], orig_string[4])
    self.assertEqual(reversed_string[2], orig_string[3])
    self.assertEqual(reversed_string[3], orig_string[2])            
    self.assertEqual(reversed_string[4], orig_string[1])    
    self.assertEqual(reversed_string[5], orig_string[0])    
   

if __name__ == '__main__':
  unittest.main()
