#!/use/bin/python3
"""
@interview
Given a list of different type, sort the integers in the list in asend order, no duplicate
"""
def list_sort_unique_asend():

  myset = set()
  mylist = [3,2,1,10,6,7,2,1,"jia",'c']
  for elem in mylist:
    if type(elem) == int:
      myset.add(elem)

  outlist = list(myset)
  outlist.sort()

  print(outlist)

def main():
  list_sort_unique_asend()

if __name__ == '__main__':
  main()