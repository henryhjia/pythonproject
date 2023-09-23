#!/usr/bin/python3
import io
import string_process_module

me = string_process_module.StringTester()

s = "5 man, a plan, a canal: Panam5"

result = me.is_string_palindrome(s)

if result:
  print('The string is palindrome')
else:
  print('The string is not a palindrome')

s = "5 man, a plan, a canal: Panam"

result = me.is_string_palindrome(s)

if result:
  print('The string is palindrome')
else:
  print('The string is not a palindrome')

s = "A man, a plan, a canal: Panama"
result = me.is_string_palindrome_method2(s)
if result:
  print('The string is palindrome')
else:
  print('The string is not a palindrome')