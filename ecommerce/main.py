#archivo main que importa la interfaz y la inicia
import tkinter as tk
from ui.tienda_app import TiendaApp

if __name__ == "__main__":
    root = tk.Tk()
    app = TiendaApp(root)
    root.mainloop()