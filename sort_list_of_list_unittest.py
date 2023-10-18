"""
sort list unittest
@sortlist unittest

usage: python3 -m unittest sort_list_unittest.UnitTest -v

"""
import unittest
import list_sort_module

class UnitTest(unittest.TestCase):
  def setUp(self):
    print('setup')
    self.me = list_sort_module.SortListModule()

  def tearDown(self):
    print('teardown')               

  def test_1_sort_list_of_list(self) -> None:

    my_list = [
      [1,2,3],
      [3,2,1],
      [2,5,5],
      [0,1,4]
    ]

    result = self.me.sort_list_of_list(my_list, 0)
    self.assertEqual(result[0][0], 0)
    self.assertEqual(result[1][0], 1)
    self.assertEqual(result[2][0], 2)
    self.assertEqual(result[3][0], 3)        

    result = self.me.sort_list_of_list(my_list, 1)
    self.assertEqual(result[0][1], 1)
    self.assertEqual(result[1][1], 2)
    self.assertEqual(result[2][1], 2)
    self.assertEqual(result[3][1], 5)        

    result = self.me.sort_list_of_list(my_list, 2)
    self.assertEqual(result[0][2], 1)
    self.assertEqual(result[1][2], 3)
    self.assertEqual(result[2][2], 4)
    self.assertEqual(result[3][2], 5)        



if __name__ == '__main__':
  unittest.main()
