"""
lambda test program
"""
from modules import common_module

class LambdaTester:
  """
  """

  def lambda_test(self):
    """
    """
    common_module.print_function(self.lambda_test)

    add = lambda x,y: x+y
    result = add(5,3)
    print(result)

    numbers = [1,2,3,4,5]

    result = map(lambda x: x**2, numbers)
    print(list(result))

    # Convert list of strings to list of integers
    string_list = ['1','2','10','20']
    result = map(lambda x: int(x), string_list)
    list_result = list(result)
    print(list_result)

    # Alternative without using lambda:
    result2 = list(map(int, string_list))
    print(result2)

    # use list comprehension:
    new_list = [int(i) for i in string_list]
    print('new_list=', new_list)

    new_list2 = [i**2 for i in numbers]
    print('new_list2=', new_list2)

def main() -> None:

  me = LambdaTester()

  me.lambda_test()


if __name__ == '__main__':
  main()