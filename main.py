import tkinter as tk
from interfaces.venta import Venta
from interfaces.almacen import Almacen
from interfaces.carrito import Carrito
from interfaces.compra import Compra
from interfaces.proveedor_crud import ProveedorCRUD
from interfaces.cliente_crud import ClientCRUD
from interfaces.usuario_crud import UserCRUD




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
        # archivo_menu.add_command(label="Carrito", command=self.open_carrito)
        archivo_menu.add_command(label="crud cliente", command=self.open_client_crud)
        archivo_menu.add_command(label="crud usuario", command=self.open_user_crud)
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

    def open_client_crud(self):
        client_crud_window = ClientCRUD(self)

    def open_user_crud(self):
        user_crud_window = UserCRUD(self)
    
    # def open_carrito(self):
    #     carrito_window = Carrito(self)
if __name__ == '__main__':
    app = PuntoDeVentaApp()
    app.mainloop()