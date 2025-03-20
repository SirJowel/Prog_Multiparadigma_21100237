class Carrito:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        if producto.stock > 0 or producto.stock == -1:  # -1 para digitales
            self.productos.append(producto)
            if producto.stock != -1:
                producto.stock -= 1
            return True
        return False

    def calcular_total(self):
        return sum(p.calcular_costo() for p in self.productos) if self.productos else 0

    def __str__(self):
        return "\n".join(str(p) for p in self.productos) or "Carrito vacío"