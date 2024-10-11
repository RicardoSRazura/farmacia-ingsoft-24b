import tkinter as tk
from tkinter import ttk

class Compra(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title('Compra de Productos')
        
        # Primera fila
        tk.Label(self, text='Folio:').grid(row=0, column=0, padx=5, pady=5)
        self.folio_entry = tk.Entry(self)
        self.folio_entry.grid(row=0, column=1, padx=5, pady=5)
        
        tk.Label(self, text='Fecha:').grid(row=0, column=2, padx=5, pady=5)
        self.fecha_entry = tk.Entry(self)
        self.fecha_entry.grid(row=0, column=3, padx=5, pady=5)
        
        # Segunda fila
        tk.Label(self, text='Proveedor:').grid(row=1, column=0, padx=5, pady=5)
        self.proveedor_combo = ttk.Combobox(self)
        self.proveedor_combo.grid(row=1, column=1, padx=5, pady=5)
        
        # Tercera fila
        tk.Label(self, text='Producto:').grid(row=2, column=0, padx=5, pady=5)
        self.producto_combo = ttk.Combobox(self)
        self.producto_combo.grid(row=2, column=1, padx=5, pady=5)
        
        self.agregar_button = tk.Button(self, text='Agregar')
        self.agregar_button.grid(row=2, column=2, padx=5, pady=5)
        
        self.quitar_button = tk.Button(self, text='Quitar')
        self.quitar_button.grid(row=2, column=3, padx=5, pady=5)
        
        # Cuarta fila
        tk.Label(self, text='Precio:').grid(row=3, column=0, padx=5, pady=5)
        self.precio_entry = tk.Entry(self)
        self.precio_entry.grid(row=3, column=1, padx=5, pady=5)
        
        # Quinta fila
        tk.Label(self, text='Cantidad:').grid(row=4, column=0, padx=5, pady=5)
        self.cantidad_entry = tk.Entry(self)
        self.cantidad_entry.grid(row=4, column=1, padx=5, pady=5)

        # Botón Carrito
        self.carrito_button = tk.Button(self, text='Carrito')
        self.carrito_button.grid(row=0, column=4, padx=5, pady=5, sticky='e')
        self.carrito_button.configure(command=self.open_carrito)

    def open_carrito(self):
        carrito_window = Carrito(self)

