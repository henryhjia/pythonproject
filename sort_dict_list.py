#!/use/bin/python3
"""
Sort dictionary and list of dictionary
list and dictionary are populated in the program
"""

class SortTester:
  """
  """
  def sort_data(self) -> None:
    """
    1. Sort a dictionary
       a. sort dic.items() so it becomes a list of tuples
       b. convert the list of tuple to a dictionary
    2. Sort list of dictionaries
       a. sort the list of dictionaires by using sort(list_of_dict, key=lambda, x:x[''] notation)
    3. Sort list of complex dictionary
    """
    print('\n*********** sort_data()')   
    print('\n*********************** sort a dictionary by value')   
    my_dict = { 
        'henry': 12, 
        'jean': 1, 
        'claire': 8, 
        'maggie': 13
      }
    print('my_dict=', my_dict)
    mylist = sorted(my_dict.items(), key=lambda x:x[1])
    print('sorted list view=', mylist)
    sorted_dict = dict(mylist)
    print('sorted_dict by value=', sorted_dict)

    print('\n*********************** sort a dictionary by key') 
    # The next two methods are the same, the second one uses default  
    # mylist = sorted(my_dict.items(), key=lambda x:x[0])
    # mylist = sorted(my_dict.items())
    mylist = sorted(my_dict.items())
    print('sorted list view=', mylist)
    sorted_dict = dict(mylist)
    print('sorted_dict by key=', sorted_dict)

    print('\n*********************** sort a list of dictionary by value')   
    my_list_of_dict = [
        {'name':'henry', 'number': 12}, 
        {'name':'jean', 'number': 1},
        {'name':'claire', 'number':8},
        {'name':'maggie', 'number':13}
    ]
    print('my_list_of_dict=', my_list_of_dict)
    sorted_list_of_dictionary = sorted(my_list_of_dict, key=lambda x:x['number'])
    print('sorted list of dictionary=', sorted_list_of_dictionary)

    print('\n*********************** sort a list of dictionary by key')   
    print('my_list_of_dict=', my_list_of_dict)
    sorted_list_of_dictionary = sorted(my_list_of_dict, key=lambda x:x['name'])
    print('sorted list of dictionary=', sorted_list_of_dictionary)

    print('\n*********************** sort a list of complex dictionary')   
    my_list_of_dict = [
        { "dad": ["henry",12,62]},
        { "mom": ["jean",1,58]},
        { "daughter": ["claire",8,30]},
        { "daughter": ["maggie",13,27]}
    ]
    print('my_list_of_dict=', my_list_of_dict)

    sorted_list = sorted(my_list_of_dict, key=lambda x:x[list(x.keys())[0]][1])     
    print('sort by value 1:', sorted_list)

    sorted_list = sorted(my_list_of_dict, key=lambda x:x[list(x.keys())[0]][2])     
    print('sort by value 2:', sorted_list)

    sorted_list = sorted(my_list_of_dict, key=lambda x:x[list(x.keys())[0]][0])     
    print('sort by value 0:', sorted_list)

    sorted_list = sorted(my_list_of_dict, key=lambda d: list(d.keys())[0])     
    print('sort by key:    ', sorted_list)


def main() -> int:

  me = SortTester()

  # sort data from variables
  me.sort_data()


if __name__ == '__main__':
  main()