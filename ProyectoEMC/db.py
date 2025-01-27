import pyodbc
class Conexion:
    def initConn(self):
        # SERVER LOCAL FKN
        user    = "admin"
        pswd    = "admin"  
        srvr    = "(localdb)\\ServidorDB"
        dbase   = "MADRID_EMC"
        
        # SERVER MADRID
        # user    = "sa"
        # pswd    = "P%40ssw0rd"  
        # srvr    = "26.145.122.242\\MSSQLSERVERENTER"
        # dbase   = "MADRID_EMC"

        # SERVER BARCELONA
        # user    = "sa"
        # pswd    = "P%40ssw0rd"  
        # srvr    = "26.225.244.188\\MSSQLSERVERENTER"
        # dbase   = "BARCELONA_EMC"
        
        self.conn = pyodbc.connect(
            f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={srvr};DATABASE={dbase};UID={user};PWD={pswd}'           
        )
        self.cursor = self.conn.cursor()
        
    def closeConn(self):
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()
    
class ServicioProveedorDAC(Conexion):          
    def getAll(self):
        super().initConn()
        result = []
        query = "SELECT * FROM SERVICIO_PROVEEDOR_01"
        self.cursor.execute(query)
        for row in self.cursor.fetchall():
            item = {
                'id_servicio': row[0],
                'id_oficina': row[1],
                'id_proveedor': row[2],
                'descripcion_ser': row[3],
                'precio_ser': row[4]
            }
            result.append(item)
        super().closeConn()
        return result
            
            
    def getById(self, id):
        super().initConn()
        result = []
        query = "SELECT * FROM SERVICIO_PROVEEDOR_01 WHERE ID_SERVICIO = ?"
        self.cursor.execute(query, id)
        for row in self.cursor.fetchall(): 
            super().closeConn()           
            result.append({
                'id_servicio': row[0],
                'id_oficina': row[1],
                'id_proveedor': row[2],
                'descripcion_ser': row[3],
                'precio_ser': row[4]
            })
            return result 
        super().closeConn()
        return None

    def add(self, item):
        super().initConn()
        query = """INSERT INTO SERVICIO_PROVEEDOR_01 
                   (ID_SERVICIO, ID_OFICINA, ID_PROVEEDOR, DESCRIPCION_SER, PRECIO_SER) 
                   VALUES (?, ?, ?, ?, ?)"""
        try:
            self.cursor.execute(
                query,
                item['id_servicio'],
                item['id_oficina'],
                item['id_proveedor'],
                item['descripcion_ser'],
                item['precio_ser'],
            )
            self.conn.commit()    
            super().closeConn()        
            return True
        except Exception as ex:
            print(f"Error capturado: {ex}")
            super().closeConn()
            return False
    
    def update(self, id, item):
        super().initConn()
        query = """UPDATE SERVICIO_PROVEEDOR_01 
                   SET ID_SERVICIO = ?, ID_OFICINA = ?, ID_PROVEEDOR = ?, DESCRIPCION_SER = ?, PRECIO_SER = ? 
                   WHERE ID_SERVICIO = ?"""                   
        try:
            self.cursor.execute(
                query,
                item['id_servicio'],
                item['id_oficina'],
                item['id_proveedor'],
                item['descripcion_ser'],
                item['precio_ser'],
                id,
            )
            self.conn.commit()
            super().closeConn()
            return True
        except Exception as ex:
            print(f"Error capturado: {ex}")
            super().closeConn()
            return False
    
    def delete(self, id):
        super().initConn()
        query = "DELETE FROM SERVICIO_PROVEEDOR_01 WHERE ID_SERVICIO = ?"
        try:
            self.cursor.execute(query, id)
            self.conn.commit()
            super().closeConn()
            return True
        except Exception as ex:
            print(f"Error capturado: {ex}")
            super().closeConn()
            return False


if __name__ == "__main__":         
    db = ServicioProveedorDAC()
    # item = {'id_servicio':'SERV007', 'id_oficina':'01', 'id_proveedor':'PROV002' , 'descripcion_ser':'Nuevo Servicio', 'precio_ser':790.5}
    # response = db.delete('SERV001')
    # print(db.getAl())
    # if response:
    #     print("eliminado")
    # else:
        # print('error')
    result = db.getById('SERV002')
    for row in result:
        print(row)