import unittest

from tire.CarriganTire import CarriganTire
import array as arr


class TestCarriganTire(unittest.TestCase):
    def test_needs_service_true(self):
        tires = arr.array(.9, .5, .9, .91)
        tire = CarriganTire(tires)
        self.assertTrue(tire.needs_service())

    def test_needs_service_false(self):
        tires = arr.array(.4, .5, .4, .5)
        
        tire = CarriganTire(tires)
        self.assertFalse(tire.needs_service())