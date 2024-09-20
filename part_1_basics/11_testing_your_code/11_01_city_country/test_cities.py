import unittest
from city_functions import city_country

class CityTestCase(unittest.TestCase):
    def test_city_country(self):
        formatted = city_country('vienna', 'austria')
        self.assertEqual(formatted, 'Vienna, Austria')

unittest.main()