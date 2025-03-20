#clase producto que servira para darle caracteristicas a los objetos
class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.__precio = precio
        self.stock = stock

    @property
    def precio(self):
        return self.__precio

    def calcular_costo(self):
        return self.precio

    def __str__(self):
        return f"{self.nombre} - ${self.precio} (Stock: {self.stock})"


class ProductoDigital(Producto):
    def __init__(self, nombre, precio):
        super().__init__(nombre, precio, -1)

    def calcular_costo(self):
        return self.precio * 0.9  # 10% de descuento

    def __str__(self):
        return f"{self.nombre} (Digital) - ${self.precio}"