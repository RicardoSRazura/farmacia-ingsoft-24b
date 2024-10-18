import tkinter as tk
from tkinter import ttk

class Registro(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title('Registro')
        self.geometry('500x300')

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(2, weight=1)

        #Frame para Entrys correo y contraseña
        self.frameEntradaDeDatos = tk.Frame(self)
        self.frameEntradaDeDatos.grid(row=1, column=1, padx=10, pady=10)

        #Entry de nombre
        self.lbNombre = tk.Label(self.frameEntradaDeDatos, text='Nombre completo: ')
        self.lbNombre.grid(row=0, column=0, padx=10, pady=10)
        self.txNombre = tk.Entry(self.frameEntradaDeDatos)
        self.txNombre.grid(row=0, column=1, padx=10, pady=10)

        #Entry de correo
        self.lbCorreo = tk.Label(self.frameEntradaDeDatos, text='Correo: ')
        self.lbCorreo.grid(row=1, column=0, padx=10, pady=10)
        self.txCorreo = tk.Entry(self.frameEntradaDeDatos)
        self.txCorreo.grid(row=1, column=1, padx=10, pady=10)

        #Entry de Contraseña
        self.lbContraseña = tk.Label(self.frameEntradaDeDatos, text='Contraseña: ')
        self.lbContraseña.grid(row=2, column=0, padx=10, pady=10)
        self.txContraseña = tk.Entry(self.frameEntradaDeDatos, show="*")
        self.txContraseña.grid(row=2, column=1, padx=10, pady=10)

        #Entry de rol
        self.lbRol = tk.Label(self.frameEntradaDeDatos, text='Rol: ')
        self.lbRol.grid(row=3, column=0, padx=10, pady=10)
        self.cbRol = ttk.Combobox(self.frameEntradaDeDatos, values=["administrador","gerente", "cajero"])
        self.cbRol.grid(row=3, column=1, padx=10, pady=10)
        self.cbRol.bind("<<ComboboxSelected>>")
        
        #Frame para los botones
        self.frameBotones = tk.Frame(self)
        self.frameBotones.grid(row=2, column=1, padx=10, pady=10)

        # self.btnLogin = tk.Button(self, text='Login')
        # self.btnLogin.grid(row=1, column=0, padx=10, pady=10, sticky='W')
        
        self.btnRegistrar = tk.Button(self.frameBotones, text='Registrar')
        self.btnRegistrar.grid(row=1, column=1, padx=10, pady=10, sticky='E')



