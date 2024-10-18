import tkinter as tk
from tkinter import ttk
from interfaces.registro import Registro
from interfaces.paginaPrincipal import PuntoDeVentaApp

class Login(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Login')
        self.geometry('300x400')

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(2, weight=1)

        #Frame para Entrys correo y contraseña
        self.frameEntradaDeDatos = tk.Frame(self)
        self.frameEntradaDeDatos.grid(row=1, column=1, padx=10, pady=10)

        #Entry de correo
        self.lbCorreo = tk.Label(self.frameEntradaDeDatos, text='Correo: ')
        self.lbCorreo.grid(row=0, column=0, padx=10, pady=10)
        self.txCorreo = tk.Entry(self.frameEntradaDeDatos)
        self.txCorreo.grid(row=0, column=1, padx=10, pady=10)

        #Entry de Contraseña
        self.lbContraseña = tk.Label(self.frameEntradaDeDatos, text='Contraseña: ')
        self.lbContraseña.grid(row=1, column=0, padx=10, pady=10)
        self.txContraseña = tk.Entry(self.frameEntradaDeDatos, show="*")
        self.txContraseña.grid(row=1, column=1, padx=10, pady=10)

        #Frame para los botones
        self.frameBotones = tk.Frame(self)
        self.frameBotones.grid(row=2, column=1, padx=10, pady=10)

        self.btnLogin = tk.Button(self.frameBotones, text='Login', command=self.abrirPantallaPrincipal)
        self.btnLogin.grid(row=1, column=0, padx=10, pady=10, sticky='W')
        
        self.btnRegistrar = tk.Button(self.frameBotones, text='Registrar', command=self.abrirRegistro)
        self.btnRegistrar.grid(row=1, column=1, padx=10, pady=10, sticky='E')

    def abrirRegistro(self):
        ventanaRegistro = Registro(self)
        ventanaRegistro.mainloop()
    
    def abrirPantallaPrincipal(self):
        # self.destroy()
        appPantallaPrincipal = PuntoDeVentaApp(self)
        appPantallaPrincipal.mainloop



