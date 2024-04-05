
from ..database.db_mysql import get_connection
from flask import request
from ..models.cliente import Cliente

class ClientService():

    @classmethod
    def get_clientes(cls):
        try: 
            connection = get_connection()
            print(connection)
        
            with connection.cursor() as cursor:
                cursor.execute('SELECT * FROM cliente')
                result= cursor.fetchall()
                print(result)
            connection.close()

            return result
        except Exception as ex:
            print(ex)

    @classmethod
    def post_client(cls, cliente: Cliente):
        try:
            connection = get_connection()

            with connection.cursor() as cursorInsert:
                dni_cliente = cliente.dni_cliente
                nombre = cliente.nombre
                email = cliente.email
                telefono = cliente.telefono
                direccion = cliente.direccion

                sql = "INSERT INTO cliente(dni_cliente, nombre, email, telefono, direccion) VALUES (%s, %s, %s, %s, %s)"
                data = (dni_cliente, nombre, email, telefono, direccion)
                cursorInsert.execute(sql, data)
            
            connection.commit()
            return data
        except Exception as ex:
       
            print("Error al insertar el clieNTE:", ex)
            return False  
    @classmethod
    def delete_client(cls,dni_cliente: int):
        try:
            connection = get_connection()
            print("esto es delete")
        
            with connection.cursor() as cursorDelete:
                    cursorDelete.execute("DELETE From cliente WHERE dni_cliente=%s", (dni_cliente,))
                
            connection.commit()
            return True
        
        except Exception as ex:    
            print("Error al eliminar el cliente:", ex)
            return False 
    @classmethod
    def editar_clientes(cls,cliente: Cliente):
        try:
            connection = get_connection()

            with connection.cursor() as cursorEdit:
                dni_cliente = cliente.dni_cliente
                nombre = cliente.nombre
                email = cliente.email
                telefono = cliente.telefono
                direccion = cliente.direccion

                sql = "UPDATE cliente SET nombre= %s, email= %s, telefono= %s, direccion= %s WHERE dni_cliente = %s"
                data = (nombre, email, telefono, direccion, dni_cliente )
                cursorEdit.execute(sql, data)
            
            connection.commit()
            return data
        except Exception as ex:
       
            print("Error al editar el clieNTE:", ex)
            return False  
            

        
   