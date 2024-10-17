import tkinter as tk
from tkinter import messagebox
from backend.clientesdb import dbClientes
from backend.usuariosdb import dbUsuario
from utils.clienteGS import Cliente

class ClientCRUD(tk.Toplevel):
    def __init__(self, parent, username, user_id):
        super().__init__(parent)
        self.username = username
        self.user_id = user_id
        self.title("Gestión de Clientes")
        self.geometry("400x500")

        # Campos de entrada
        self.id_label = tk.Label(self, text="ID")
        self.id_label.pack(anchor='w')
        self.txId = tk.Entry(self)
        self.txId.pack(anchor='w')
        self.nombre_label = tk.Label(self, text="Nombre")
        self.nombre_label.pack(anchor='w')
        self.txNombreCliente = tk.Entry(self)
        self.txNombreCliente.pack(anchor='w')
        self.puntos_acumulados_label = tk.Label(self, text="Puntos Acumulados")
        self.puntos_acumulados_label.pack(anchor='w')
        self.txPuntosAcumulados = tk.Entry(self)
        self.txPuntosAcumulados.pack(anchor='w')

        # Campos de usuario
        self.usuario_id_label = tk.Label(self, text="ID del Usuario")
        self.usuario_id_label.pack(anchor='w')
        self.txUsuarioId = tk.Entry(self, state='readonly')
        self.txUsuarioId.pack(anchor='w')
        self.usuario_nombre_label = tk.Label(self, text="Nombre del Usuario")
        self.usuario_nombre_label.pack(anchor='w')
        self.txUsuarioNombre = tk.Entry(self, state='readonly')
        self.txUsuarioNombre.pack(anchor='w')

        # Botones
        self.btNuevo = tk.Button(self, text="Nuevo", command=self.nuevo_cliente)
        self.btNuevo.pack(side=tk.LEFT, padx=5, pady=5)
        self.btSalvar = tk.Button(self, text="Salvar", command=self.salvar_cliente)
        self.btSalvar.pack(side=tk.LEFT, padx=5, pady=5)
        self.btSalvar.config(state=tk.DISABLED)
        self.btCancelar = tk.Button(self, text="Cancelar", command=self.cancelar)
        self.btCancelar.pack(side=tk.LEFT, padx=5, pady=5)
        self.btCancelar.config(state=tk.DISABLED)
        self.btEditar = tk.Button(self, text="Editar", command=self.editar_cliente)
        self.btEditar.pack(side=tk.LEFT, padx=5, pady=5)
        self.btEditar.config(state=tk.DISABLED)
        self.btEliminar = tk.Button(self, text="Eliminar", command=self.eliminar_cliente)
        self.btEliminar.pack(side=tk.LEFT, padx=5, pady=5)
        self.btEliminar.config(state=tk.DISABLED)

        # Campo de búsqueda
        self.buscar_label = tk.Label(self, text="Buscar ID")
        self.buscar_label.pack(anchor='center')
        self.txIngresarId = tk.Entry(self)
        self.txIngresarId.pack(anchor='center')
        self.btBuscar = tk.Button(self, text="Buscar", command=self.buscar_cliente)
        self.btBuscar.pack(anchor='center')

    def nuevo_cliente(self):
        self.txId.delete(0, tk.END)
        self.txNombreCliente.delete(0, tk.END)
        self.txPuntosAcumulados.delete(0, tk.END)
        self.txUsuarioId.config(state=tk.NORMAL)
        self.txUsuarioId.delete(0, tk.END)
        self.txUsuarioId.config(state='readonly')
        self.txUsuarioNombre.config(state=tk.NORMAL)
        self.txUsuarioNombre.delete(0, tk.END)
        self.txUsuarioNombre.config(state='readonly')
        db_clientes = dbClientes()
        nuevo_id = db_clientes.getMaxId() + 1
        self.txId.insert(0, nuevo_id)
        self.btSalvar.config(state=tk.NORMAL)
        self.btCancelar.config(state=tk.NORMAL)
        self.btEditar.config(state=tk.DISABLED)
        self.btEliminar.config(state=tk.DISABLED)

    def salvar_cliente(self):
        nombre = self.txNombreCliente.get()
        puntos_acumulados = self.txPuntosAcumulados.get()
        if not nombre or not puntos_acumulados:
            messagebox.showerror("Error", "Todos los campos son obligatorios")
            return
        cliente = Cliente()
        cliente.setNombre(nombre)
        cliente.setPuntosAcumulados(puntos_acumulados)
        db_clientes = dbClientes()
        db_clientes.save(cliente, self.user_id)
        messagebox.showinfo("Éxito", "Cliente guardado exitosamente")
        self.nuevo_cliente()

    def cancelar(self):
        self.nuevo_cliente()

    def editar_cliente(self):
        cliente_id = self.txId.get()
        nombre = self.txNombreCliente.get()
        puntos_acumulados = self.txPuntosAcumulados.get()
        if not cliente_id or not nombre or not puntos_acumulados:
            messagebox.showerror("Error", "Todos los campos son obligatorios")
            return
        cliente = Cliente()
        cliente.setIdCliente(cliente_id)
        cliente.setNombre(nombre)
        cliente.setPuntosAcumulados(puntos_acumulados)
        db_clientes = dbClientes()
        db_clientes.edit(cliente)
        messagebox.showinfo("Éxito", "Cliente editado exitosamente")
        self.nuevo_cliente()

    def eliminar_cliente(self):
        cliente_id = self.txId.get()
        if not cliente_id:
            messagebox.showerror("Error", "ID del cliente es necesario para eliminar")
            return
        db_clientes = dbClientes()
        db_clientes.remov(cliente_id)
        messagebox.showinfo("Éxito", "Cliente eliminado exitosamente")
        self.nuevo_cliente()

    def buscar_cliente(self):
        cliente_id = self.txIngresarId.get()
        if not cliente_id:
            messagebox.showerror("Error", "ID del cliente es necesario para buscar")
            return
        db_clientes = dbClientes()
        cliente = db_clientes.search(cliente_id)
        if cliente:
            self.txId.delete(0, tk.END)
            self.txId.insert(0, cliente.getIdCliente())
            self.txNombreCliente.delete(0, tk.END)
            self.txNombreCliente.insert(0, cliente.getNombre())
            self.txPuntosAcumulados.delete(0, tk.END)
            self.txPuntosAcumulados.insert(0, cliente.getPuntosAcumulados())

            # Obtener información del usuario que registró el cliente
            db_usuario = dbUsuario()
            usuario = db_usuario.search(cliente.getUsuario_id())
            if usuario:
                self.txUsuarioId.config(state=tk.NORMAL)
                self.txUsuarioId.delete(0, tk.END)
                self.txUsuarioId.insert(0, usuario.getUsuario_id())
                self.txUsuarioId.config(state='readonly')
                self.txUsuarioNombre.config(state=tk.NORMAL)
                self.txUsuarioNombre.delete(0, tk.END)
                self.txUsuarioNombre.insert(0, usuario.getNombre())
                self.txUsuarioNombre.config(state='readonly')
            self.btEditar.config(state=tk.NORMAL)
            self.btCancelar.config(state=tk.NORMAL)
            self.btEliminar.config(state=tk.NORMAL)
        else:
            messagebox.showerror("Error", "Cliente no encontrado")
