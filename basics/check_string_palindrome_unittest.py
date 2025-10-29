"""
check if a string is a palindrome unittest
@getwordcount unittest

usage: python3 -m unittest check_string_palindrome_unittest.UnitTest -v

"""
import io
import unittest
import string_process_module

class UnitTest(unittest.TestCase):
  def setUp(self):
    print('setup')
    self.me = string_process_module.StringProcessModule()

  def tearDown(self):
    print('teardown')          

  def test_1_is_string_palindrome(self) -> None:
    s = "5 man, a plan, a canal: Panam5"
    result = self.me.is_string_palindrome(s)
    self.assertTrue(result)

    s = "5 man, a plan, a canal: Panam"
    result = self.me.is_string_palindrome(s)
    self.assertFalse(result)

  def test_2_is_string_palindrome_method2(self) -> None:
    s = "A man, a plan, a canal: Panama"
    result = self.me.is_string_palindrome_method2(s)
    self.assertTrue(result)

if __name__ == '__main__':
  unittest.main()
