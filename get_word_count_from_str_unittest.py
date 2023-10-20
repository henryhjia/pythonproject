"""
count occurence word from string unittest
@getwordcount unittest

usage: python3 -m unittest get_word_count_from_str_unittest.UnitTest -v

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

  def test_1_count_occurrence(self) -> None:
    stream = io.StringIO("Hey! How are you?\nI am good, how about you?\nI am good too.")
    word = 'good'
    result = self.me.count_occurrence(word, stream)
    self.assertEqual(result, 2)

if __name__ == '__main__':
  unittest.main()
