#!/use/bin/python3
"""
Python practice

"""

class Practice:
  """
  @brief
  """

  def __init__(self) -> None:
    """
    @brief constructor
    """
    pass


  def amazon_exam(self, repo_list: list, cus_query: str) -> list:
    ""
    print('\n*********** amazon_exam()')

    lower_repo_list = []
    for i in repo_list:
      print(i, i.lower())
      lower_repo_list.append(i.lower())

    print('lower_repo_list=', lower_repo_list)
    output_list = []
    each_list = []
    a = ''
    for i in range (0, len(cus_query)):
      a = a + cus_query[i]
      if i>=1:
        each_list.clear()
        for item in lower_repo_list:
          if item.startswith(a) and len(each_list) <=2:
            each_list.append(item)
      output_list.append(each_list.copy())

    return output_list    

  
def main() -> None:
  """
  """

  me = Practice()

  # amazon test
  repository = ['mobile','mouse','moneypot','Monitor','mousepad']
  customerQuery = 'Mouse'

  result = me.amazon_exam(repository, customerQuery.lower())
  print('result=', result)
  for i in result:
    print(i)

if __name__ == '__main__':
  main()
