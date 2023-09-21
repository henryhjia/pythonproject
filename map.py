#!/use/bin/python3
"""
map test program
"""


class MapTester:
  """
  """

  def square(self):
    """
    """

    numbers = [1,2,3,4,5]
    squared_numbers = map(lambda x: x**2, numbers)
    print(squared_numbers)
    print('squared_number list=', list(squared_numbers))

  def cheaptest(self):
    store1=[10.00,11.00,12.34,2.34]
    store2=[9.00,11.10,12.34,2.01]

    cheap = map(min, store1, store2)
    print('cheap=', cheap)
    for i in cheap:
      print(i)
      
def main() -> int:

  me = MapTester()

  me.square()
  me.cheaptest()

if __name__ == '__main__':
  main()