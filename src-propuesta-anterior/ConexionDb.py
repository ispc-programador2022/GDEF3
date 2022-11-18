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

    def insertarDato(self, celular):
        if self.conexion.is_connected():
            cursor = self.conexion.cursor()
            querySql = "INSERT INTO [dbo].Celulares VALUES (%s,%s,%s,%s)"
            data = (celular.marca, celular.nombre, celular.codigo, celular.precio)
            cursor.execute(querySql, data)

            self.conexion.commit()
            cursor.close()
            self.conexion.close()

    def modificarDato(self, celular):
        if self.conexion.is_connected():
            cursor = self.conexion.cursor()
            querySql = f"""UPDATE [dbo].Celulares SET
                        Marca = {celular.marca}
                        Nombre = {celular.nombre}
                        Codigo = {celular.codigo}
                        Precio = {celular.precio}"""
            cursor.execute(querySql)

            self.conexion.commit()
            cursor.close()
            self.conexion.close()

    def eliminarDato(self, id):
        if self.conexion.is_connected():
            cursor = self.conexion.cursor()
            querySql = f"""DELETE FROM [dbo].Celulares 
                        WHERE CelularId = {id}"""
            cursor.execute(querySql)

            self.conexion.commit()
            cursor.close()
            self.conexion.close()

    def obtenerDato(self, id):
        if self.conexion.is_connected():
            cursor = self.conexion.cursor()
            querySql = f"""SELECT * FROM [dbo].Celulares 
                        WHERE CelularId = {id}"""
            cursor.execute(querySql)

            dato = cursor.fetchone()
            self.conexion.commit()
            cursor.close()
            self.conexion.close()

            return dato