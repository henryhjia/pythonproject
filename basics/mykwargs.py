# key words arguments usage example
def example_function(**kwargs):
  for key, value in kwargs.items():
    print(f'{key}: {value}')

  for key in kwargs:
    print(key)

  for value in kwargs.values():
    print(value)  

  print(sorted(kwargs.items()))

def example_start_args(*args):
  print('example_start_args')
  for arg in args:
    print(arg)

example_function(name='ALice', age = 30, city = 'Chicago')  

example_start_args(1, 2, 3)