import unittest
from models.producto import Producto, ProductoDigital
from models.carrito import Carrito


class TestCarrito(unittest.TestCase):
    def setUp(self):
        self.carrito = Carrito()
        self.producto_fisico = Producto("Libro", 20.0, 5)
        self.producto_digital = ProductoDigital("Ebook", 15.0)

    def test_carrito_vacio(self):
        self.assertEqual(len(self.carrito.productos), 0)
        self.assertEqual(self.carrito.calcular_total(), 0)

    def test_agregar_producto_fisico(self):
        self.assertTrue(self.carrito.agregar_producto(self.producto_fisico))
        self.assertEqual(len(self.carrito.productos), 1)
        self.assertEqual(self.carrito.calcular_total(), 20.0)

    def test_agregar_producto_digital(self):
        self.assertTrue(self.carrito.agregar_producto(self.producto_digital))
        self.assertEqual(len(self.carrito.productos), 1)
        self.assertEqual(self.carrito.calcular_total(), 13.5)  # 15.0 * 0.9

    def test_agregar_producto_sin_stock(self):
        producto_sin_stock = Producto("Lápiz", 2.0, 0)
        self.assertFalse(self.carrito.agregar_producto(producto_sin_stock))
        self.assertEqual(len(self.carrito.productos), 0)


if __name__ == "__main__":
    unittest.main()