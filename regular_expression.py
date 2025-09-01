#!/use/bin/python3
"""
@regularexpression
"""
import re
from modules import common_module

def email_validation():
  """
  A valid email address meets the following criteria:

  It's composed of a username, domain name, and extension assembled in this format: 
  username@domain.extension
  The username starts with an English alphabetical character, and any subsequent 
  characters consist of one or more of the following: alphanumeric characters, -,., and _.

  The domain and extension contain only English alphabetical characters.
  The extension is 1, 2, or 3 characters in length.

  @emailvalidation
  @validateemail
  @regularexpression
  """
  common_module.print_function(email_validation)
  email_list = [
  '<alice-b@google.com>',
  '<Henry.jia_12@Gmail.com>',
  "<dexter@hotmail.cm>",
  "<virus!@variable.:p>",
  "<itsallcrap>",
  "<harsh_1234@rediff.in>",
  "<kunal_shin@iop.az>",
  "<matt23@@india.in>",
  '<.harsh_1234@rediff.in>'
  ]

  pattern = r'^<[a-zA-Z][a-zA-Z0-9-._]*@[a-zA-Z]+\.[a-z|A-Z]{1,3}>$'

  email_size = len(email_list)

  for str in email_list:
    match = re.search(pattern, str)
    if match:
      print(f'{str:30s} {match.group()}')  
    else:
      print(f'{str:30s} no match')

def phone_number_validation():
  """
  A valid mobile number is a ten digit number starting with a 7,8 or 9.
  @regularexpression
  @validatephoneumber
  @phonevalidation
  @phonenumbervalidation
  """
  common_module.print_function(phone_number_validation)

  pattern = r'^[7-9]\d{9}$'

  phone_list = [
    "9587456281",
    "1252478965",
    "87453231",
    "987rtd90fd",
    "131231",
    "85234789651"
  ]

  list_size = len(phone_list)

  for phone in phone_list:
    match = re.search(pattern, phone)
    if match:
      print(f'{phone:30s} {match.group()}')
    else:
      print(f'{phone:30s} no match')

def validate_names():
  """
  """
  common_module.print_function(validate_names)

  pattern = r'\b[A-Z][a-z]*\b'
  text = 'Amy is 5 years old, and her sister Mary is 2 years old. Ruth and Peter, their parents, have 3 kids'

  match = re.findall(pattern, text)
  print(match)

def validate_credit_card():
  """
  """
  common_module.print_function(validate_credit_card)

  pattern = r'^\d{4}-\d{4}-\d{4}-\d{4}$'
  text = '1234-5678-9012-3456'

  match = re.findall(pattern, text)
  print(match)

def reg_tester():
  common_module.print_function(reg_tester)

  text = "Amy works well, Amy gets good grades.  Our student Amy is good"

  result = re.split('Amy', text)
  print(result)
  
  result = re.findall('Amy', text)
  print(result)

  result = re.search("^Amy", text)
  print(result)

  grades="ACAAAABCBCBAA"
  print(re.findall("[AB]", grades))
  print(re.findall('A{2,10}', grades))
  print(re.findall('A{1,1}A{1,1}', grades))
  print(re.findall('A{1,2}', grades))
  print(re.findall('[a-zA-Z ]*', text))
  print(re.split('[,.]', text))

  

def main():
  email_validation()
  phone_number_validation()
  validate_names()
  validate_credit_card()
  reg_tester()

if __name__ == '__main__':
  main()
