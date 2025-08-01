"""
Reverse list unittest
@reverselist unittest

usage: python3 -m unittest reverse_list_unittest.UnitTest -v

reverse a list : three methods
1. looping
2. list.reverse() method - in place reverse
3. slicing
"""
import unittest
from modules import list_process_module

class UnitTest(unittest.TestCase):
  def setUp(self):
    print('setup')
    self.me = list_process_module.ListProcessModule()

  def tearDown(self):
    print('teardown')

  def test_1_reverse_by_coding(self):

    # reverse list 
    list1 = [2,4,5,8]
    list2 = self.me.reverse_list_using_looping(list1)

    self.assertEqual(list1[0], list2[3])
    self.assertEqual(list1[1], list2[2])
    self.assertEqual(list1[2], list2[1])
    self.assertEqual(list1[3], list2[0])            

  def test_2_reverse_inplace(self):

    # reverse list 
    list1 = [2,4,5,8]
    list2 = list(list1)
    list1.reverse()
    
    self.assertEqual(list1[0], list2[3])
    self.assertEqual(list1[1], list2[2])
    self.assertEqual(list1[2], list2[1])
    self.assertEqual(list1[3], list2[0])      

  def test_3_reverse_list_using_slicing(self):

    # reverse list 
    list1 = [2,4,5,8]
    list2 = self.me.reverse_list_using_slicing(list1)

    self.assertEqual(list1[0], list2[3])
    self.assertEqual(list1[1], list2[2])
    self.assertEqual(list1[2], list2[1])
    self.assertEqual(list1[3], list2[0])      



if __name__ == '__main__':
  unittest.main()
