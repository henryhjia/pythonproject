# key words arguments usage example
def example_function(**kwargs):
  for key, value in kwargs.items():
    print(f'{key}: {value}')

example_function(name='ALice', age = 30, city = 'Chicago')