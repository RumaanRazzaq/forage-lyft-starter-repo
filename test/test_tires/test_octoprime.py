import unittest

from tyres.octoprime_tyres import OctoprimeTyres

class TestOctoprime(unittest.TestCase):
    def test_tyre_should_be_serviced(self):
        tyre_wear = [1, 1.2, 0.7, 0.1]
        tyres = OctoprimeTyres(tyre_wear)
        self.assertTrue(tyres.needs_service())

    def test_tyre_should_not_be_serviced(self):
        tyre_wear = [1, 1, 0.8, 0.15]
        tyres = OctoprimeTyres(tyre_wear)
        self.assertFalse(tyres.needs_service())

if __name__ == '__main__':
    unittest.main()