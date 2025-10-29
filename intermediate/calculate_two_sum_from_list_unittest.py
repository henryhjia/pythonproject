"""
calculate two sum unittest
@towsum unittest

usage: python3 -m unittest calculate_two_sum_from_list_unittest.UnitTest -v

"""
import unittest
import two_sum_module

class UnitTest(unittest.TestCase):
  def setUp(self):
    print('setup')
    self.me = two_sum_module.TwoSumModule()

  def tearDown(self):
    print('teardown')

  def test_1_find_two_sum_equal_to_target(self):
    in_list = [1,2,3]
    target = 5
    result = self.me.find_two_sum_equal_to_target(in_list, target)
   
    self.assertEqual(result[0], 2)
    self.assertEqual(result[1], 3)    

if __name__ == '__main__':
  unittest.main()
