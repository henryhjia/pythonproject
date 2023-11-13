"""
Reorder a list of tuples so one can travel from the starting city to the ending city

"""
import common_module

class CityTravelModule:
  """
  """

  def __init__(self, in_list: list):
    self._inlist = in_list

  def find_starting_city(self) -> str:
    """
    """
    l1 = []
    l2 = []

    for i in self._inlist:
      l1.append(i[0])
      l2.append(i[1])

    start_city = ''
    for city in l1:
      if city not in l2:
        start_city = city
        break

    return start_city

  def construct_city_travel_list(self, start_city) -> list:
    """
    """
    list_len = len(self._inlist)
    city_list = []

    city_list.append(start_city)

    i = 0
    while i < list_len:
      for item in self._inlist:
        if item[0] == start_city:
          city_list.append(item[1])
          start_city = item[1]
      i += 1
    
    return city_list