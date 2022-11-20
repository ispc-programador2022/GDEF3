import mysql, mysql.connector
from mysql.connector import Error

class Conexion:
    def __init__(self) -> None:
        try:
            self.conexion = mysql.connector.connect(host='localhost',
                                                port = '3306',
                                                database='GDEF3',
                                                user='gdef3',
                                                password='gdef123')
        except Error as e:
            print("Error while connecting to MySQL", e)

    def insertarDato(self, panial):
        if self.conexion.is_connected():
            cursor = self.conexion.cursor()
            querySql = "INSERT INTO [dbo].Panial VALUES (%s,%s,%s,%s)"
            data = (panial.marca.marcaId, celular.tipo.tipoID, celular.precio, celular.cantidad)
            cursor.execute(querySql, data)

            self.conexion.commit()
            cursor.close()
            self.conexion.close()

    def modificarDato(self, panial):
        if self.conexion.is_connected():
            cursor = self.conexion.cursor()
            querySql = f"""UPDATE [dbo].Panial SET
                        MarcaId = {panial.marcaId}
                        Nombre = {panial.tipo.tipoId}
                        Precio = {panial.precio}
                        Cantidad = {panial.cantidad}"""
            cursor.execute(querySql)

            self.conexion.commit()
            cursor.close()
            self.conexion.close()

    def eliminarDato(self, id):
        if self.conexion.is_connected():
            cursor = self.conexion.cursor()
            querySql = f"""DELETE FROM [dbo].Panial 
                        WHERE PanialId = {id}"""
            cursor.execute(querySql)

            self.conexion.commit()
            cursor.close()
            self.conexion.close()

    def obtenerDato(self, id):
        if self.conexion.is_connected():
            cursor = self.conexion.cursor()
            querySql = f"""SELECT * FROM [dbo].Panial 
                        WHERE PanialId = {id}"""
            cursor.execute(querySql)

            dato = cursor.fetchone()
            self.conexion.commit()
            cursor.close()
            self.conexion.close()

            return dato