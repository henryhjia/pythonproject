#!/use/bin/python3
"""
list comprehension test program
"""


class ListComprehensionsTester:
  """
  """

  def square(self):
    """
    """
    numbers = [1,2,3,4,5]

    result = [x**3 for x in range(21) if x%2]
    print(result)

    result = [x**3 for x in range(21) if x%2 == 0]
    print(result)

    squared_numbers = [x**2 for x in numbers]
    print(squared_numbers)

    squared_numbers = [x for x in numbers if x % 2 ==0]
    print(squared_numbers)

    new_list = [number for number in range(0,100) if number %2 ==0]
    print(new_list)
    
def main() -> int:

  me = ListComprehensionsTester()

  me.square()


if __name__ == '__main__':
  main()