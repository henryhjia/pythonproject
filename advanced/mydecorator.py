def make_pretty(func):
  # define the inner function
  def inner():
    print('I got decorated')

    func()

  return inner


#method 1:
# def ordinary():
#   print('I am ordinary')

# decorated_func = make_pretty(ordinary)
# decorated_func()

#method 2:
@make_pretty
def ordinary():
  print('I am ordinary')

ordinary()