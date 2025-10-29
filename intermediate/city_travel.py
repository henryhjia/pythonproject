"""
"""
import city_travel_module

def main():
  """
  """

  input_list_tuple = [('Bergerac', 'Pau'), ('Nice', 'Montpellier'), ('Pau', 'Paris'), ('Marseille', 'Nice'), ('Montpellier', 'Bergerac')]

  me = city_travel_module.CityTravelModule(input_list_tuple)

  start_city = me.find_starting_city()

  city_travel_list = me.construct_city_travel_list(start_city)
  print('city travel list=', city_travel_list)

if __name__ == "__main__":
  main()