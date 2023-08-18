import unittest

from tyres.carrigan_tyres import CarriganTyres

class TestCarrigan(unittest.TestCase):
    def test_tyre_should_be_serviced(self):
        tyre_wear = [0.1, 0.2, 0.3, 0.9]
        tyres = CarriganTyres(tyre_wear)
        self.assertTrue(tyres.needs_service())

    def test_tyre_should_not_be_serviced(self):
        tyre_wear = [0.1, 0.2, 0.3, 0.04]
        tyres = CarriganTyres(tyre_wear)
        self.assertFalse(tyres.needs_service())

if __name__ == '__main__':
    unittest.main()