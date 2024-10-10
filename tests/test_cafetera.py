import unittest
from cafetera import Cafetera

class TestCafetera(unittest.TestCase):
    def setUp(self):
        self.cafetera = Cafetera()

    def test_hay_vasos_pequenos(self):
        self.assertTrue(self.cafetera.hay_vasos("pequeño"))

    def test_no_hay_vasos_pequenos(self):
        self.cafetera.vasos_pequenos = 0
        self.assertFalse(self.cafetera.hay_vasos("pequeño"))

    def test_restar_cafe(self):
        self.cafetera.servir_cafe("pequeño", 5)
        self.assertEqual(self.cafetera.cafe, 45)

    def test_restar_vaso(self):
        self.cafetera.servir_cafe("pequeño", 5)
        self.assertEqual(self.cafetera.vasos_pequenos, 9)

    def test_no_hay_vasos(self):
        self.cafetera.vasos_pequenos = 0
        mensaje = self.cafetera.servir_cafe("pequeño", 5)
        self.assertEqual(mensaje, "No hay vasos de tipo pequeño")

    def test_no_hay_cafe(self):
        self.cafetera.cafe = 3
        mensaje = self.cafetera.servir_cafe("pequeño", 5)
        self.assertEqual(mensaje, "No hay suficiente café")

if __name__ == '__main__':
    unittest.main()
