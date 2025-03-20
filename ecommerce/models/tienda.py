class Tienda:
    def __init__(self):
        self.catalogo = []

    def agregar_al_catalogo(self, producto):
        self.catalogo.append(producto)

    def buscar_producto(self, nombre):
        for producto in self.catalogo:
            if producto.nombre == nombre:
                return producto
        return None

    def realizar_compra(self, cliente, carrito):
        if not carrito.productos:
            return "Compra cancelada: carrito vacío."
        total = carrito.calcular_total()
        return f"Compra de {cliente}:\n{carrito}\nTotal: ${total}"