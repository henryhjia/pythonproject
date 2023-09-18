#!/use/bin/python3
"""
test program
"""

class User:
  def __init__(self, name, email):
    self._name = name
    self._email = email

  def get_name(self):
    return self._name

  def get_email(self):
    return self._email

  def do_something(self):
    print('Hi from ' + self._name)

  def __str__(self):
    return self._name + ', ', + self._email

  def print_alpha_nums(self, abc_list, num_list):
    for char in abc_list:
      for num in num_list:
        print(char,num)


def main():
  users = [ User('henry', 'h@gmail.com'), User('jean','j@gmail.com')]
  for user in users:
    user.do_something()
    user.print_alpha_nums(['a','b','c'], [1,2,3])

if __name__ == '__main__':
  main()
