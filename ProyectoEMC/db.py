import pyodbc

class ServicioProveedorDAC:
    def initConn(self):
        self.conn = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};SERVER=(localdb)\ServidorDB;DATABASE=MADRID_EMC;UID=admin;PWD=admin'
        )
        self.cursor = self.conn.cursor()
        
    def closeConn(self):
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()
        
    def getAll(self):
        self.initConn()
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
        self.closeConn
        return result
            
            
    def getById(self, id):
        self.initConn()
        query = "SELECT * FROM SERVICIO_PROVEEDOR_01 WHERE ID_SERVICIO = ?"
        self.cursor.execute(query, id)
        for row in self.cursor.fetchall(): 
            self.closeConn()           
            return {
                'id_servicio': row[0],
                'id_oficina': row[1],
                'id_proveedor': row[2],
                'descripcion_ser': row[3],
                'precio_ser': row[4]
            }
        self.closeConn()
        return None

    def add(self, item):
        self.initConn()
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
            self.closeConn()        
            return True
        except Exception as ex:
            print(f"Error capturado: {ex}")
            self.closeConn()
            return False
    
    def modify(self, id, item):
        self.initConn()
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
            self.closeConn()
            return True
        except Exception as ex:
            print(f"Error capturado: {ex}")
            self.closeConn()
            return False
    
    def delete(self, id):
        query = "DELETE FROM SERVICIO_PROVEEDOR_01 WHERE ID_SERVICIO = ?"
        try:
            self.cursor.execute(query, id)
            self.conn.commit()
            self.closeConn()
            return True
        except Exception as ex:
            print(f"Error capturado: {ex}")
            self.closeConn()
            return False


# if __name__ == "__main__":         
    # db = ServicioProveedorDAC()
    # item = {'id_servicio':'SERV007', 'id_oficina':'01', 'id_proveedor':'PROV002' , 'descripcion_ser':'Nuevo Servicio', 'precio_ser':790.5}
    # response = db.delete('SERV001')
    # # print(db.getAl())
    # if response:
    #     print("eliminado")
    # else:
    #     print('error')
    # print(db.getAll())