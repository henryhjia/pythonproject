#!/use/bin/python3
"""
map test program
"""

def mapfunction(x):
  return x+1

class MapTester:
  """
  """

  def square(self):
    """
    """

    numbers = [1,2,3,4,5]
    print(f'origin numbers     = {numbers}')

    squared_numbers = map(lambda x: x**2, numbers)
    print(f'squared_number list= {list(squared_numbers)}')

    plusone = map(mapfunction, numbers)
    print(f'plus one result    = {list(plusone)}')

  def cheaptest(self):
    store1=[10.00,11.00,12.34,2.34]
    store2=[9.00,11.10,12.34,2.01]

    cheap = map(min, store1, store2)
    print('min of each list =')
    for i in cheap:
      print(i)
      
def main() -> int:

  me = MapTester()

  me.square()
  me.cheaptest()

if __name__ == '__main__':
  main()