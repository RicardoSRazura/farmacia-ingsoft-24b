import tkinter as tk
from venta import Venta
from carrito import Carrito
from compra import Compra
from proveedor_crud import ProveedorCRUD
from almacen import Almacen


class PuntoDeVentaApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Punto de Venta')
        self.geometry('400x300')
        
        # Menú principal
        menubar = tk.Menu(self)
        self.config(menu=menubar)
        
        archivo_menu = tk.Menu(menubar, tearoff=0)
        archivo_menu.add_command(label="Venta", command=self.open_venta)
        archivo_menu.add_command(label="Compra", command=self.open_compra)
        archivo_menu.add_command(label="Gestión de Proveedores", command=self.open_proveedor_crud)
        archivo_menu.add_command(label="Almacén", command=self.open_almacen)
        archivo_menu.add_separator()
        archivo_menu.add_command(label="Salir", command=self.quit)
        menubar.add_cascade(label="Archivo", menu=archivo_menu)

    def open_venta(self):
        venta_window = Venta(self)

    def open_compra(self):
        compra_window = Compra(self)

    def open_proveedor_crud(self):
        proveedor_crud_window = ProveedorCRUD(self)

    def open_almacen(self):
        almacen_window = Almacen(self)

if __name__ == '__main__':
    app = PuntoDeVentaApp()
    app.mainloop()
