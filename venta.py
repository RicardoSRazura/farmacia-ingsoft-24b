import tkinter as tk
from tkinter import ttk

class Venta(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title('Venta de Productos')
        
        # Primera fila
        tk.Label(self, text='Folio:').grid(row=0, column=0, padx=5, pady=5)
        self.folio_entry = tk.Entry(self)
        self.folio_entry.grid(row=0, column=1, padx=5, pady=5)
        
        tk.Label(self, text='Fecha:').grid(row=0, column=2, padx=5, pady=5)
        self.fecha_entry = tk.Entry(self)
        self.fecha_entry.grid(row=0, column=3, padx=5, pady=5)
        
        # Segunda fila
        tk.Label(self, text='Buscar Producto:').grid(row=1, column=0, padx=5, pady=5)
        self.producto_entry = tk.Entry(self)
        self.producto_entry.grid(row=1, column=1, padx=5, pady=5)
        
        self.buscar_button = tk.Button(self, text='Buscar')
        self.buscar_button.grid(row=1, column=2, padx=5, pady=5)
        
        # Tercera fila
        tk.Label(self, text='Código:').grid(row=2, column=0, padx=5, pady=5)
        self.codigo_entry = tk.Entry(self)
        self.codigo_entry.grid(row=2, column=1, padx=5, pady=5)
        
        # Cuarta fila
        tk.Label(self, text='Nombre de Producto:').grid(row=3, column=0, padx=5, pady=5)
        self.nombre_entry = tk.Entry(self)
        self.nombre_entry.grid(row=3, column=1, padx=5, pady=5)
        
        # Quinta fila
        tk.Label(self, text='Descripción:').grid(row=4, column=0, padx=5, pady=5)
        self.descripcion_entry = tk.Entry(self)
        self.descripcion_entry.grid(row=4, column=1, padx=5, pady=5)
        
        # Sexta fila
        tk.Label(self, text='Precio:').grid(row=5, column=0, padx=5, pady=5)
        self.precio_entry = tk.Entry(self)
        self.precio_entry.grid(row=5, column=1, padx=5, pady=5)
        
        # Séptima fila
        tk.Label(self, text='Stock:').grid(row=6, column=0, padx=5, pady=5)
        self.stock_entry = tk.Entry(self)
        self.stock_entry.grid(row=6, column=1, padx=5, pady=5)
        
        # Octava fila
        tk.Label(self, text='Cantidad:').grid(row=7, column=0, padx=5, pady=5)
        self.cantidad_entry = tk.Entry(self)
        self.cantidad_entry.grid(row=7, column=1, padx=5, pady=5)
        
        self.agregar_button = tk.Button(self, text='Agregar')
        self.agregar_button.grid(row=7, column=2, padx=5, pady=5)
        
        self.quitar_button = tk.Button(self, text='Quitar')
        self.quitar_button.grid(row=7, column=3, padx=5, pady=5)
        
        self.cancelar_button = tk.Button(self, text='Cancelar Venta')
        self.cancelar_button.grid(row=7, column=4, padx=5, pady=5)

        # Botón Carrito
        self.carrito_button = tk.Button(self, text='Carrito')
        self.carrito_button.grid(row=0, column=5, padx=5, pady=5, sticky='e')
        self.carrito_button.configure(command=self.open_carrito)

        # Cuadro para Cliente
        self.cliente_frame = tk.LabelFrame(self, text='Cliente')
        self.cliente_frame.grid(row=0, column=6, rowspan=8, padx=10, pady=5, sticky='nsew')
        
        tk.Label(self.cliente_frame, text='Codigo del cliente:').grid(row=0, column=0, padx=5, pady=5)
        self.nombre_cliente_entry = tk.Entry(self.cliente_frame)
        self.nombre_cliente_entry.grid(row=0, column=1, padx=5, pady=5)
        
        tk.Label(self.cliente_frame, text='Seleccionar Cliente:').grid(row=1, column=0, padx=5, pady=5)
        self.clientes_combo = ttk.Combobox(self.cliente_frame)
        self.clientes_combo.grid(row=1, column=1, padx=5, pady=5)
        
        tk.Label(self.cliente_frame, text='RFC:').grid(row=2, column=0, padx=5, pady=5)
        self.rfc_entry = tk.Entry(self.cliente_frame)
        self.rfc_entry.grid(row=2, column=1, padx=5, pady=5)



    def open_carrito(self):
        carrito_window = Carrito(self)
