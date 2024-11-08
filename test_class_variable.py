"""
test class variable and instance variable
@classvariable
@instancevariable
"""

class User:
  class_var1 = 1

  def __init__(self, name, email, count):
    self._name = name
    self._email = email
    self._count = count

  def get_name(self):
    return self._name

  def get_email(self):
    return self._email

  def do_something(self):
    print('Instance variable from ' + self._name + ' is: ' + str(self._count))

  def __str__(self):
    return self._name + ', ', + self._email

def main():
  users = [ User('david', 'd@gmail.com', 3), User('katie','k@gmail.com',1 )]
  for user in users:
    user.do_something()
    print('Class variable=', User.class_var1)

main()
