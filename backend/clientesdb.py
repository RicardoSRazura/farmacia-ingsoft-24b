import mysql.connector
from mysql.connector import Error
import conexion as con
from utils.clienteGs import Cliente

class dbClientes:
    def get_all(self):
        try:
            conn = con.conexion().open()
            cursor = conn.cursor()
            cursor.execute("SELECT id_cliente, nombre FROM clientes")
            clientes = cursor.fetchall()
            conn.close()
            return [Cliente(id_cliente=row[0], nombre=row[1]) for row in clientes]
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return []

    def save(self, cliente, usuario_id):
        try:
            self.con = con.conexion()
            self.conn = self.con.open()
            if self.conn is None:
                raise Exception("No se pudo conectar a la base de datos")
            self.cursor = self.conn.cursor()
            self.sql = "INSERT INTO clientes (nombre, puntos_acumulados, usuario_id) VALUES (%s, %s, %s)"
            self.datos = (cliente.getNombre(), cliente.getPuntosAcumulados(), usuario_id)
            self.cursor.execute(self.sql, self.datos)
            self.conn.commit()
            print("Datos insertados correctamente")
            self.con.close()
        except mysql.connector.Error as err:
            print(f"Error al guardar el cliente: {err}")
        except Exception as e:
            print(f"Error: {e}")

    def search(self, cliente_id):
        try:
            self.con = con.conexion()
            self.conn = self.con.open()
            self.cursor = self.conn.cursor(buffered=True)
            self.sql = "SELECT * FROM clientes WHERE id_cliente = %s"
            self.cursor.execute(self.sql, (cliente_id,))
            row = self.cursor.fetchone()
            self.con.close()
            if row:
                cliente = Cliente(row[0], row[1], row[2], row[3])
                return cliente
            return None
        except mysql.connector.Error as err:
            print(f"Error al buscar el cliente: {err}")
            return None

    def edit(self, cliente):
        try:
            self.con = con.conexion()
            self.conn = self.con.open()
            self.cursor = self.conn.cursor()
            self.sql = "UPDATE clientes SET nombre=%s, puntos_acumulados=%s WHERE id_cliente=%s"
            self.datos = (cliente.getNombre(), cliente.getPuntosAcumulados(), cliente.getIdCliente())
            self.cursor.execute(self.sql, self.datos)
            self.conn.commit()
            self.con.close()
        except mysql.connector.Error as err:
            print(f"Error al editar el cliente: {err}")

    def remov(self, cliente_id):
        try:
            self.con = con.conexion()
            self.conn = self.con.open()
            self.cursor = self.conn.cursor()
            self.sql = "DELETE FROM clientes WHERE id_cliente=%s"
            self.cursor.execute(self.sql, (cliente_id,))
            self.conn.commit()
            self.con.close()
        except mysql.connector.Error as err:
            print(f"Error al eliminar el cliente: {err}")

    def getMaxId(self):
        try:
            self.con = con.conexion()
            self.conn = self.con.open()
            self.cursor = self.conn.cursor()
            self.sql = "SELECT MAX(id_cliente) FROM clientes"
            self.cursor.execute(self.sql)
            row = self.cursor.fetchone()
            self.con.close()
            return row[0] if row[0] is not None else 0
        except mysql.connector.Error as err:
            print(f"Error al obtener el máximo ID: {err}")
            return 0
