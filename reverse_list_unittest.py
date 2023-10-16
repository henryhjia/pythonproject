#!/use/bin/python3
"""
Reverse list unittest
@reverselist unittest

usage: python3 -m unittest reverse_list_unittest.UnitTest -v

reverse a list : three methods
1. manual
2. slicing
3. list.reverse() method - in place reverse
"""
import unittest
import list_process_module

class UnitTest(unittest.TestCase):

  def test_1_reverse_by_coding(self):

    me = list_process_module.ProcessList()

    # reverse list 
    list1 = [2,4,5,8]
    list2 = me.reverse_list_by_coding(list1)
    list3 = me.reverse_list_by_coding(list2)
    self.assertEqual(list1, list3)

  def test_2_reverse_inplace(self):

    me = list_process_module.ProcessList()

    # reverse list 
    list1 = [2,4,5,8]
    list2 = list(list1)
    list1.reverse()
    
    self.assertNotEqual(list1, list2)

  def test_3_reverse_inplace(self):

    me = list_process_module.ProcessList()

    # reverse list 
    list1 = [2,4,5,8]
    list2 = me.reverse_list_using_slicing(list1)
    
    self.assertNotEqual(list1, list2)


if __name__ == '__main__':
  unittest.main()
