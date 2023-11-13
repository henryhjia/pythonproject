"""
city travel unittest
usage: python3 -m unittest city_travel_unittest.UnitTest -v
"""
import city_travel_module
import unittest

class UnitTest(unittest.TestCase):

  def setUp(self):
    inlist = [('Bergerac', 'Pau'), ('Nice', 'Montpellier'), ('Pau', 'Paris'), ('Marseille', 'Nice'), ('Montpellier', 'Bergerac')]
    self.me = city_travel_module.CityTravelModule(inlist)

  def tearDown(self):
    pass

  def test_1_find_starting_city(self) -> None:

    start_city = self.me.find_starting_city()
    self.assertEqual(start_city, 'Marseille')

  def test_2_construct_city_travel_list(self) -> None:

    city_list = self.me.construct_city_travel_list('Marseille')

    self.assertEqual(city_list[0], 'Marseille')
    self.assertEqual(city_list[1], 'Nice')
    self.assertEqual(city_list[2], 'Montpellier')
    self.assertEqual(city_list[3], 'Bergerac')
    self.assertEqual(city_list[4], 'Pau')    
    self.assertEqual(city_list[5], 'Paris')                  

if __name__ == '__main__':
  unittest.main()