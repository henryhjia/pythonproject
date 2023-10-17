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

  def test_1_sort_sorted(self) -> None:
    l1 = [10, 9,4,6,20,1]
    l2 = self.me.sort_sorted(l1)

    self.assertEqual(len(l1), len(l2))
    self.assertEqual(l2[0], 1)
    self.assertEqual(l2[1], 4)
    self.assertEqual(l2[2], 6)
    self.assertEqual(l2[3], 9)
    self.assertEqual(l2[4], 10)
    self.assertEqual(l2[5], 20)

  def test_2_sort_sorted(self) -> None:
    l1 = ['henry', 'bob', 'jack', 'kate']
    l2 = self.me.sort_sorted(l1)

    self.assertEqual(len(l1), len(l2))
    self.assertEqual(l2[0], 'bob')
    self.assertEqual(l2[1], 'henry')
    self.assertEqual(l2[2], 'jack')
    self.assertEqual(l2[3], 'kate')

  def test_3_sort_in_place_sort(self) -> None:
    l1 = [10, 9,4,6,20,1]
    l2 = self.me.sort_in_place_sort(l1)

    self.assertEqual(len(l1), len(l2))
    self.assertEqual(l1[0], 1)
    self.assertEqual(l1[1], 4)
    self.assertEqual(l1[2], 6)
    self.assertEqual(l1[3], 9)
    self.assertEqual(l1[4], 10)
    self.assertEqual(l1[5], 20)

    self.assertEqual(l2[0], 1)
    self.assertEqual(l2[1], 4)
    self.assertEqual(l2[2], 6)
    self.assertEqual(l2[3], 9)
    self.assertEqual(l2[4], 10)
    self.assertEqual(l2[5], 20)

  def test_4_sort_in_place_sort(self) -> None:
    l1 = ['henry', 'bob', 'jack', 'kate']
    l2 = self.me.sort_in_place_sort(l1)

    self.assertEqual(len(l1), len(l2))
    self.assertEqual(l1[0], 'bob')
    self.assertEqual(l1[1], 'henry')
    self.assertEqual(l1[2], 'jack')
    self.assertEqual(l1[3], 'kate')

    self.assertEqual(l2[0], 'bob')
    self.assertEqual(l2[1], 'henry')
    self.assertEqual(l2[2], 'jack')
    self.assertEqual(l2[3], 'kate')

  def test_5_sort_integer_unique_mixed_data_type_in_list(self) -> None:
    mylist = [3,2,1,10,6,7,2,1,"jia",'c']
    result = self.me.sort_integer_unique_mixed_data_type_in_list(mylist)

    self.assertEqual(len(result), 6)
    self.assertEqual(result[0], 1)
    self.assertEqual(result[1], 2)
    self.assertEqual(result[2], 3)
    self.assertEqual(result[3], 6)
    self.assertEqual(result[4], 7)
    self.assertEqual(result[5], 10)                


if __name__ == '__main__':
  unittest.main()
