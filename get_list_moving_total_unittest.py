"""
get list moving total unittest
@listmovingtotal unittest

usage: python3 -m unittest get_list_moving_total_unittest.UnitTest -v

"""
import unittest
import list_process_module

class UnitTest(unittest.TestCase):
  def setUp(self):
    print('setup')
    self.me = list_process_module.ListProcessModule()

  def tearDown(self):
    print('teardown')          

  def test_1_list_moving_total_contains(self) -> None:
    result = self.me.list_moving_total_contains([1, 2, 3, 4], 3, 6)    
    self.assertTrue(result)      

    result = self.me.list_moving_total_contains([1, 2, 3, 4], 3, 9)
    self.assertTrue(result)     

    result = self.me.list_moving_total_contains([1, 2, 3, 4], 3, 12)    
    self.assertFalse(result)         

    result = self.me.list_moving_total_contains([1, 2, 3, 4], 3, 7)    
    self.assertFalse(result)         

    result = self.me.list_moving_total_contains([1, 2, 3, 4, 5], 3, 6) 
    self.assertTrue(result)         

    result = self.me.list_moving_total_contains([1, 2, 3, 4, 5], 3, 9)    
    self.assertTrue(result)         

    result = self.me.list_moving_total_contains([1, 2, 3, 4, 5], 3, 12)    
    self.assertTrue(result)         

    result = self.me.list_moving_total_contains([1, 2, 3, 4, 5], 3, 7)    
    self.assertFalse(result)   

if __name__ == '__main__':
  unittest.main()
