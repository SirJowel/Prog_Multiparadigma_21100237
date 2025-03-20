import tkinter as tk
from tkinter import ttk, messagebox
from models.producto import Producto, ProductoDigital
from models.cliente import Cliente
from models.carrito import Carrito
from models.tienda import Tienda


class TiendaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Tienda Online")
        self.tienda = Tienda()
        self.carrito = Carrito()
        self.cliente = None

        # Crear pestañas
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(fill=tk.BOTH, expand=True)

        # Pestaña de cliente
        self.tab_cliente = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_cliente, text="Cliente")

        self.label_nombre_cliente = tk.Label(self.tab_cliente, text="Nombre:")
        self.label_nombre_cliente.grid(row=0, column=0, padx=10, pady=10)
        self.entry_nombre_cliente = tk.Entry(self.tab_cliente)
        self.entry_nombre_cliente.grid(row=0, column=1, padx=10, pady=10)

        self.label_email_cliente = tk.Label(self.tab_cliente, text="Email:")
        self.label_email_cliente.grid(row=1, column=0, padx=10, pady=10)
        self.entry_email_cliente = tk.Entry(self.tab_cliente)
        self.entry_email_cliente.grid(row=1, column=1, padx=10, pady=10)

        self.button_agregar_cliente = tk.Button(
            self.tab_cliente, text="Agregar cliente", command=self.agregar_cliente
        )
        self.button_agregar_cliente.grid(row=2, column=0, padx=10, pady=10)

        self.button_desbloquear_cliente = tk.Button(
            self.tab_cliente, text="Editar cliente", command=self.desbloquear_cliente, state=tk.DISABLED
        )
        self.button_desbloquear_cliente.grid(row=2, column=1, padx=10, pady=10)

        # Pestaña de catálogo
        self.tab_catalogo = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_catalogo, text="Catálogo")

        self.label_nombre = tk.Label(self.tab_catalogo, text="Nombre:")
        self.label_nombre.grid(row=0, column=0, padx=10, pady=10)
        self.entry_nombre = tk.Entry(self.tab_catalogo)
        self.entry_nombre.grid(row=0, column=1, padx=10, pady=10)

        self.label_precio = tk.Label(self.tab_catalogo, text="Precio:")
        self.label_precio.grid(row=1, column=0, padx=10, pady=10)
        self.entry_precio = tk.Entry(self.tab_catalogo)
        self.entry_precio.grid(row=1, column=1, padx=10, pady=10)

        self.label_stock = tk.Label(self.tab_catalogo, text="Stock:")
        self.label_stock.grid(row=2, column=0, padx=10, pady=10)
        self.entry_stock = tk.Entry(self.tab_catalogo)
        self.entry_stock.grid(row=2, column=1, padx=10, pady=10)

        self.es_digital = tk.BooleanVar()
        self.check_digital = tk.Checkbutton(
            self.tab_catalogo, text="Producto digital", variable=self.es_digital, command=self.toggle_stock_field
        )
        self.check_digital.grid(row=3, column=0, columnspan=2, pady=10)

        self.button_agregar_catalogo = tk.Button(
            self.tab_catalogo, text="Agregar al catálogo", command=self.agregar_al_catalogo
        )
        self.button_agregar_catalogo.grid(row=4, column=0, columnspan=2, pady=10)

        # Pestaña de carrito
        self.tab_carrito = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_carrito, text="Carrito")

        self.label_producto = tk.Label(self.tab_carrito, text="Seleccionar producto:")
        self.label_producto.grid(row=0, column=0, padx=10, pady=10)
        self.combo_productos = ttk.Combobox(self.tab_carrito, state="readonly")
        self.combo_productos.grid(row=0, column=1, padx=10, pady=10)

        self.button_agregar_carrito = tk.Button(
            self.tab_carrito, text="Agregar al carrito", command=self.agregar_al_carrito
        )
        self.button_agregar_carrito.grid(row=1, column=0, columnspan=2, pady=10)

        self.label_carrito = tk.Label(self.tab_carrito, text="Contenido del carrito:")
        self.label_carrito.grid(row=2, column=0, padx=10, pady=10)
        self.text_carrito = tk.Text(self.tab_carrito, height=10, width=40)
        self.text_carrito.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

        self.button_realizar_compra = tk.Button(
            self.tab_carrito, text="Realizar compra", command=self.realizar_compra
        )
        self.button_realizar_compra.grid(row=4, column=0, columnspan=2, pady=10)

    def toggle_stock_field(self):
        # Activar o desactivar el campo de stock según el estado del checkbox
        if self.es_digital.get():
            self.entry_stock.config(state=tk.DISABLED)
        else:
            self.entry_stock.config(state=tk.NORMAL)

    def agregar_cliente(self):
        nombre = self.entry_nombre_cliente.get()
        email = self.entry_email_cliente.get()
        if nombre and email:
            self.cliente = Cliente(nombre, email)
            messagebox.showinfo("Éxito", "Cliente agregado correctamente.")
            self.bloquear_campos_cliente()
        else:
            messagebox.showwarning("Error", "Por favor, completa todos los campos.")

    def bloquear_campos_cliente(self):
        # Bloquear campos y habilitar el botón de desbloquear
        self.entry_nombre_cliente.config(state=tk.DISABLED)
        self.entry_email_cliente.config(state=tk.DISABLED)
        self.button_agregar_cliente.config(state=tk.DISABLED)
        self.button_desbloquear_cliente.config(state=tk.NORMAL)

    def desbloquear_cliente(self):
        # Desbloquear campos y limpiar los datos
        self.entry_nombre_cliente.config(state=tk.NORMAL)
        self.entry_email_cliente.config(state=tk.NORMAL)
        self.button_agregar_cliente.config(state=tk.NORMAL)
        self.button_desbloquear_cliente.config(state=tk.DISABLED)
        self.entry_nombre_cliente.delete(0, tk.END)
        self.entry_email_cliente.delete(0, tk.END)
        self.cliente = None

    def agregar_al_catalogo(self):
        nombre = self.entry_nombre.get()
        precio = float(self.entry_precio.get())
        stock = int(self.entry_stock.get()) if not self.es_digital.get() else -1
        if self.es_digital.get():
            producto = ProductoDigital(nombre, precio)
        else:
            producto = Producto(nombre, precio, stock)
        self.tienda.agregar_al_catalogo(producto)
        self.actualizar_combobox()
        self.limpiar_campos_catalogo()

    def agregar_al_carrito(self):
        nombre = self.combo_productos.get()
        producto = self.tienda.buscar_producto(nombre)
        if producto:
            if self.carrito.agregar_producto(producto):
                self.actualizar_carrito()
            else:
                messagebox.showwarning("Error", f"No hay stock de {producto.nombre}.")
        else:
            messagebox.showwarning("Error", "Producto no encontrado.")

    def actualizar_combobox(self):
        productos = [producto.nombre for producto in self.tienda.catalogo]
        self.combo_productos["values"] = productos

    def actualizar_carrito(self):
        self.text_carrito.delete(1.0, tk.END)
        self.text_carrito.insert(tk.END, str(self.carrito))

    def realizar_compra(self):
        if not self.cliente:
            messagebox.showwarning("Error", "Primero agrega un cliente.")
            return
        if not self.carrito.productos:
            messagebox.showwarning("Error", "El carrito está vacío.")
            return
        
        # Usar el método realizar_compra de la clase Tienda
        resumen_compra = self.tienda.realizar_compra(self.cliente, self.carrito)
        messagebox.showinfo("Resumen de la compra", resumen_compra)
        
        # Reiniciar el carrito después de la compra
        self.carrito = Carrito()
        self.actualizar_carrito()

    def limpiar_campos_catalogo(self):
        self.entry_nombre.delete(0, tk.END)
        self.entry_precio.delete(0, tk.END)
        self.entry_stock.delete(0, tk.END)
        self.es_digital.set(False)
