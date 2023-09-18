#!/usr/bin/python3
# Get sum of a sub list by slicing the list
class MovingTotal:

    def __init__(self):
        self._mylist = []
        self._mysumlist = []
        
    def append(self, numbers):
        """
        :param numbers: (list) The list of numbers.
        """
        for i in numbers:
            self._mylist.append(i)

        pass

    def contains(self, total):
        """
        :param total: (int) The total to check for.
        :returns: (bool) If MovingTotal contains the total.
        """
        list_len = len(self._mylist)
        print(self._mylist)
        mysum = 0
        for i in range(list_len):
          if i+3 <= list_len:
              sub_list = self._mylist[i:i+3]
              mysum = sum(sub_list)
              self._mysumlist.append(mysum)
              mysum = 0
       
        ret_value = False
        for item in self._mysumlist:
            if item == total:
                ret_value = True

        return ret_value
    
if __name__ == "__main__":
    movingtotal = MovingTotal()
    
    movingtotal.append([1, 2, 3, 4])
    print(movingtotal.contains(6))
    print(movingtotal.contains(9))
    print(movingtotal.contains(12))
    print(movingtotal.contains(7))
    
    movingtotal.append([5])
    print(movingtotal.contains(6))
    print(movingtotal.contains(9))
    print(movingtotal.contains(12))
    print(movingtotal.contains(7))