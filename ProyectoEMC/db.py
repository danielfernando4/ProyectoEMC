import pyodbc
class Conexion:
    def __init__(self):
        self.id_oficina = '02'
        
    def initConn(self):            
        # SERVER LOCAL FKN
        #user    = "admin"
        #pswd    = "admin"  
        #srvr    = "(localdb)\\ServidorDB"
        #dbase   = "MADRID_EMC"
        
        # SERVER MADRID
        # user    = "sa"
        # pswd    = "P@ssw0rd"  
        # srvr    = "26.145.122.242\\MSSQLSERVERENTER"
        # dbase   = "MADRID_EMC"

        # SERVER BARCELONA
        user    = "sa"
        pswd    = "P@ssw0rd"  
        srvr    = "26.225.244.188\\MSSQLSERVERENTER"
        dbase   = "BARCELONA_EMC"
        
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
        query = f"SELECT * FROM SERVICIO_PROVEEDOR_{self.id_oficina}"
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
        query = f"SELECT * FROM SERVICIO_PROVEEDOR_{self.id_oficina} WHERE ID_SERVICIO = ?"
        print(query)
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
        query = f"""INSERT INTO SERVICIO_PROVEEDOR_{self.id_oficina} 
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
    
    def update(self, item):
        super().initConn()
        query = f"""UPDATE SERVICIO_PROVEEDOR_{self.id_oficina} 
                   SET ID_PROVEEDOR = ?, DESCRIPCION_SER = ?, PRECIO_SER = ? 
                   WHERE ID_SERVICIO = ?"""                   
        try:
            self.cursor.execute(
                query,
                item['id_proveedor'],
                item['descripcion_ser'],
                item['precio_ser'],
                item['id_servicio']
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
        query = f"DELETE FROM SERVICIO_PROVEEDOR_{self.id_oficina} WHERE ID_SERVICIO = ?"
        try:
            self.cursor.execute(query, id)
            self.conn.commit()
            super().closeConn()
            return True
        except Exception as ex:
            print(f"Error capturado: {ex}")
            super().closeConn()
            return False


class ClienteDAC(Conexion):
    def getAll(self):
        super().initConn()
        result = []
        query = f"SELECT * FROM CLIENTE"
        self.cursor.execute(query)
        for row in self.cursor.fetchall():
            item = {
                'id_cliente': row[0],
                'nombre_cl': row[1],
                'apellido_cl': row[2],
                'correo_cl': row[3],
                'telefono_cl': row[4],
                'direccion_cl': row[5]
            }
            result.append(item)
        super().closeConn()
        return result

    def getById(self, id):
        super().initConn()
        result = []
        query = f"SELECT * FROM CLIENTE WHERE ID_CLIENTE = ?"
        self.cursor.execute(query, id)
        row = self.cursor.fetchone()
        super().closeConn()
        if row:
            result.append({
                'id_cliente': row[0],
                'nombre_cl': row[1],
                'apellido_cl': row[2],
                'correo_cl': row[3],
                'telefono_cl': row[4],
                'direccion_cl': row[5]
            })
            return result
        return None

    def add(self, item):
        super().initConn()
        query = f"""INSERT INTO CLIENTE (ID_CLIENTE, NOMBRE_CL, APELLIDO_CL, CORREO_CL, TELEFONO_CL, DIRECCION_CL) 
                   VALUES (?, ?, ?, ?, ?, ?)"""
        try:
            self.cursor.execute(
                query,
                item['id_cliente'],
                item['nombre_cl'],
                item['apellido_cl'],
                item['correo_cl'],
                item['telefono_cl'],
                item['direccion_cl']
            )
            self.conn.commit()
            super().closeConn()
            return True
        except Exception as ex:
            print(f"Error capturado: {ex}")
            super().closeConn()
            return False

    def update(self, item):
        super().initConn()
        query = f"""UPDATE CLIENTE 
                   SET NOMBRE_CL = ?, APELLIDO_CL = ?, CORREO_CL = ?, TELEFONO_CL = ?, DIRECCION_CL = ? 
                   WHERE ID_CLIENTE = ?"""
        try:
            self.cursor.execute(
                query,
                item['nombre_cl'],
                item['apellido_cl'],
                item['correo_cl'],
                item['telefono_cl'],
                item['direccion_cl'],
                item['id_cliente']
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
        query = f"DELETE FROM CLIENTE WHERE ID_CLIENTE = ?"
        try:
            self.cursor.execute(query, id)
            self.conn.commit()
            super().closeConn()
            return True
        except Exception as ex:
            print(f"Error capturado: {ex}")
            super().closeConn()
            return False


class ContratoEventoDAC(Conexion):
    def getAll(self):
        super().initConn()
        result = []
        query = f"SELECT * FROM CONTRATO_EVENTO_{self.id_oficina}"
        self.cursor.execute(query)
        for row in self.cursor.fetchall():
            item = {
                'id_contrato': row[0],
                'id_oficina': row[1],
                'id_evento': row[2],
                'id_empleado': row[3],
                'id_cliente': row[4],
                'id_servicio': row[5],
                'fecha_inicio': row[6],
                'fecha_fin': row[7],
                'presupuesto': row[8],
                'lugar': row[9],
                'estado_contrato': row[10]
            }
            result.append(item)
        super().closeConn()
        return result

    def getById(self, id_contrato):
        super().initConn()
        result = []
        query = f"SELECT * FROM CONTRATO_EVENTO_{self.id_oficina} WHERE ID_CONTRATO = ?"
        self.cursor.execute(query, (id_contrato))
        row = self.cursor.fetchone()
        super().closeConn()
        if row:
            result.append({
                'id_contrato': row[0],
                'id_oficina': row[1],
                'id_evento': row[2],
                'id_empleado': row[3],
                'id_cliente': row[4],
                'id_servicio': row[5],
                'fecha_inicio': row[6],
                'fecha_fin': row[7],
                'presupuesto': row[8],
                'lugar': row[9],
                'estado_contrato': row[10]
            })
            return result
        return None

    def add(self, item):
        super().initConn()
        query = f"""INSERT INTO CONTRATO_EVENTO_{self.id_oficina} 
                   (ID_CONTRATO, ID_OFICINA, ID_EVENTO, ID_EMPLEADO, ID_CLIENTE, ID_SERVICIO, 
                    FECHA_INICIO, FECHA_FIN, PRESUPUESTO, LUGAR, ESTADO_CONTRATO) 
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"""
        try:
            self.cursor.execute(
                query,
                item['id_contrato'],
                item['id_oficina'],
                item['id_evento'],
                item['id_empleado'],
                item['id_cliente'],
                item['id_servicio'],
                item['fecha_inicio'],
                item['fecha_fin'],
                item['presupuesto'],
                item['lugar'],
                item['estado_contrato']
            )
            self.conn.commit()
            super().closeConn()
            return True
        except Exception as ex:
            print(f"Error capturado: {ex}")
            super().closeConn()
            return False

    def update(self, item):
        super().initConn()
        query = f"""UPDATE CONTRATO_EVENTO_{self.id_oficina} 
                   SET ID_EVENTO = ?, ID_EMPLEADO = ?, ID_CLIENTE = ?, ID_SERVICIO = ?, 
                       FECHA_INICIO = ?, FECHA_FIN = ?, PRESUPUESTO = ?, LUGAR = ?, ESTADO_CONTRATO = ? 
                   WHERE ID_CONTRATO = ?"""
        try:
            self.cursor.execute(
                query,
                item['id_evento'],
                item['id_empleado'],
                item['id_cliente'],
                item['id_servicio'],
                item['fecha_inicio'],
                item['fecha_fin'],
                item['presupuesto'],
                item['lugar'],
                item['estado_contrato'],
                item['id_contrato']
            )
            self.conn.commit()
            super().closeConn()
            return True
        except Exception as ex:
            print(f"Error capturado: {ex}")
            super().closeConn()
            return False

    def delete(self, id_contrato):
        super().initConn()
        query = f"DELETE FROM CONTRATO_EVENTO_{self.id_oficina} WHERE ID_CONTRATO = ?"
        try:
            self.cursor.execute(query, (id_contrato))
            self.conn.commit()
            super().closeConn()
            return True
        except Exception as ex:
            print(f"Error capturado: {ex}")
            super().closeConn()
            return False


class EmpleadoDAC(Conexion):
    def getAll(self):
        super().initConn()
        result = []
        query = f"SELECT * FROM EMPLEADO_{self.id_oficina}"
        self.cursor.execute(query)
        for row in self.cursor.fetchall():
            item = {
                'id_empleado': row[0],
                'id_oficina': row[1],
                'nombre_emp': row[2],
                'apellido_emp': row[3],
                'cargo_emp': row[4],
                'telefono_emp': row[5],
                'correo_emp': row[6]
            }
            result.append(item)
        super().closeConn()
        return result

    def getById(self, id_empleado):
        super().initConn()
        result = []
        query = f"SELECT * FROM EMPLEADO_{self.id_oficina} WHERE ID_EMPLEADO = ?"
        self.cursor.execute(query, (id_empleado))
        row = self.cursor.fetchone()
        super().closeConn()
        if row:
            result.append({
                'id_empleado': row[0],
                'id_oficina': row[1],
                'nombre_emp': row[2],
                'apellido_emp': row[3],
                'cargo_emp': row[4],
                'telefono_emp': row[5],
                'correo_emp': row[6]
            })
            return result
        return None

    def add(self, item):
        super().initConn()
        query = f"""INSERT INTO EMPLEADO_{self.id_oficina} 
                   (ID_EMPLEADO, ID_OFICINA, NOMBRE_EMP, APELLIDO_EMP, CARGO_EMP, TELEFONO_EMP, CORREO_EMP) 
                   VALUES (?, ?, ?, ?, ?, ?, ?)"""
        try:
            self.cursor.execute(
                query,
                item['id_empleado'],
                item['id_oficina'],
                item['nombre_emp'],
                item['apellido_emp'],
                item['cargo_emp'],
                item['telefono_emp'],
                item['correo_emp']
            )
            self.conn.commit()
            super().closeConn()
            return True
        except Exception as ex:
            print(f"Error capturado: {ex}")
            super().closeConn()
            return False

    def update(self, item):
        super().initConn()
        query = f"""UPDATE EMPLEADO_{self.id_oficina} 
                   SET NOMBRE_EMP = ?, APELLIDO_EMP = ?, CARGO_EMP = ?, TELEFONO_EMP = ?, CORREO_EMP = ? 
                   WHERE ID_EMPLEADO = ?"""
        try:
            self.cursor.execute(
                query,
                item['nombre_emp'],
                item['apellido_emp'],
                item['cargo_emp'],
                item['telefono_emp'],
                item['correo_emp'],
                item['id_empleado']
            )
            self.conn.commit()
            super().closeConn()
            return True
        except Exception as ex:
            print(f"Error capturado: {ex}")
            super().closeConn()
            return False

    def delete(self, id_empleado):
        super().initConn()
        query = f"DELETE FROM EMPLEADO_{self.id_oficina} WHERE ID_EMPLEADO = ?"
        try:
            self.cursor.execute(query, (id_empleado))
            self.conn.commit()
            super().closeConn()
            return True
        except Exception as ex:
            print(f"Error capturado: {ex}")
            super().closeConn()
            return False


class NominaDAC(Conexion):
    def getAll(self):
        super().initConn()
        result = []
        query = f"SELECT * FROM NOMINA_EMPLEADO"
        self.cursor.execute(query)
        for row in self.cursor.fetchall():
            item = {
                'id_empleado': row[0],
                'salario': row[1],
                'fecha_contratacion': row[2]
            }
            result.append(item)
        super().closeConn()
        return result

    def getById(self, id_empleado):
        super().initConn()
        result = []
        query = f"SELECT * FROM NOMINA_EMPLEADO WHERE ID_EMPLEADO = ?"
        self.cursor.execute(query, (id_empleado))
        row = self.cursor.fetchone()
        super().closeConn()
        if row:
            result.append({
                'id_empleado': row[0],
                'salario': row[1],
                'fecha_contratacion': row[2]
            })
            return result
        return None

    def add(self, item):
        super().initConn()
        query = f"""INSERT INTO NOMINA_EMPLEADO 
                   (ID_EMPLEADO, SALARIO, FECHA_CONTRATACION) 
                   VALUES (?, ?, ?)"""
        try:
            self.cursor.execute(
                query,
                item['id_empleado'],
                item['salario'],
                item['fecha_contratacion']
            )
            self.conn.commit()
            super().closeConn()
            return True
        except Exception as ex:
            print(f"Error capturado: {ex}")
            super().closeConn()
            return False

    def update(self, item):
        super().initConn()
        query = f"""UPDATE NOMINA_EMPLEADO
                   SET SALARIO = ?, FECHA_CONTRATACION = ? 
                   WHERE ID_EMPLEADO = ?"""
        try:
            self.cursor.execute(
                query,
                item['salario'],
                item['fecha_contratacion'],
                item['id_empleado']
            )
            self.conn.commit()
            super().closeConn()
            return True
        except Exception as ex:
            print(f"Error capturado: {ex}")
            super().closeConn()
            return False

    def delete(self, id_empleado):
        super().initConn()
        query = f"DELETE FROM NOMINA_EMPLEADO WHERE ID_EMPLEADO = ?"
        try:
            self.cursor.execute(query, (id_empleado))
            self.conn.commit()
            super().closeConn()
            return True
        except Exception as ex:
            print(f"Error capturado: {ex}")
            super().closeConn()
            return False


class EventoDAC(Conexion):
    def getAll(self):
        super().initConn()
        result = []
        query = f"SELECT * FROM EVENTO_{self.id_oficina}"
        self.cursor.execute(query)
        for row in self.cursor.fetchall():
            item = {
                'id_evento': row[0],
                'id_oficina': row[1],
                'tipo_evento': row[2],
                'costo_referencial': row[3]
            }
            result.append(item)
        super().closeConn()
        return result

    def getById(self, id_evento):
        super().initConn()
        result = []
        query = f"SELECT * FROM EVENTO_{self.id_oficina} WHERE ID_EVENTO = ?"
        self.cursor.execute(query, (id_evento,))
        row = self.cursor.fetchone()
        super().closeConn()
        if row:
            result.append({
                'id_evento': row[0],
                'id_oficina': row[1],
                'tipo_evento': row[2],
                'costo_referencial': row[3]
            })
            return result
        return None

    def add(self, item):
        super().initConn()
        query = f"""INSERT INTO EVENTO_{self.id_oficina} 
                   (ID_EVENTO, ID_OFICINA, TIPO_EVENTO, COSTO_REFERENCIAL) 
                   VALUES (?, ?, ?, ?)"""
        try:
            self.cursor.execute(
                query,
                item['id_evento'],
                item['id_oficina'],
                item['tipo_evento'],
                item['costo_referencial']
            )
            self.conn.commit()
            super().closeConn()
            return True
        except Exception as ex:
            print(f"Error capturado: {ex}")
            super().closeConn()
            return False

    def update(self, item):
        super().initConn()
        query = f"""UPDATE EVENTO_{self.id_oficina} 
                   SET TIPO_EVENTO = ?, COSTO_REFERENCIAL = ?
                   WHERE ID_EVENTO = ?"""
        try:
            self.cursor.execute(
                query,
                item['tipo_evento'],
                item['costo_referencial'],
                item['id_evento']
            )
            self.conn.commit()
            super().closeConn()
            return True
        except Exception as ex:
            print(f"Error capturado: {ex}")
            super().closeConn()
            return False

    def delete(self, id_evento):
        super().initConn()
        query = f"DELETE FROM EVENTO_{self.id_oficina} WHERE ID_EVENTO = ?"
        try:
            self.cursor.execute(query, (id_evento))
            self.conn.commit()
            super().closeConn()
            return True
        except Exception as ex:
            print(f"Error capturado: {ex}")
            super().closeConn()
            return False


class ProveedorDAC(Conexion):
    def getAll(self):
        super().initConn()
        result = []
        query = f"SELECT * FROM PROVEEDOR_{self.id_oficina}"
        self.cursor.execute(query)
        for row in self.cursor.fetchall():
            item = {
                'id_proveedor': row[0],
                'id_oficina': row[1],
                'nombre_pro': row[2],
                'especialidad_pro': row[3]
            }
            result.append(item)
        super().closeConn()
        return result

    def getById(self, id_proveedor):
        super().initConn()
        result = []
        query = f"SELECT * FROM PROVEEDOR_{self.id_oficina} WHERE ID_PROVEEDOR = ?"
        self.cursor.execute(query, (id_proveedor))
        row = self.cursor.fetchone()
        super().closeConn()
        if row:
            result.append({
                'id_proveedor': row[0],
                'id_oficina': row[1],
                'nombre_pro': row[2],
                'especialidad_pro': row[3]
            })
            return result
        return None

    def add(self, item):
        super().initConn()
        query = f"""INSERT INTO PROVEEDOR_{self.id_oficina} 
                   (ID_PROVEEDOR, ID_OFICINA, NOMBRE_PRO, ESPECIALIDAD_PRO) 
                   VALUES (?, ?, ?, ?)"""
        try:
            self.cursor.execute(
                query,
                item['id_proveedor'],
                item['id_oficina'],
                item['nombre_pro'],
                item['especialidad_pro']
            )
            self.conn.commit()
            super().closeConn()
            return True
        except Exception as ex:
            print(f"Error capturado: {ex}")
            super().closeConn()
            return False

    def update(self, item):
        super().initConn()
        query = f"""UPDATE PROVEEDOR_{self.id_oficina} 
                   SET NOMBRE_PRO = ?, ESPECIALIDAD_PRO = ? 
                   WHERE ID_PROVEEDOR = ?"""
        try:
            self.cursor.execute(
                query,
                item['nombre_pro'],
                item['especialidad_pro'],
                item['id_proveedor']
            )
            self.conn.commit()
            super().closeConn()
            return True
        except Exception as ex:
            print(f"Error capturado: {ex}")
            super().closeConn()
            return False

    def delete(self, id_proveedor):
        super().initConn()
        query = f"DELETE FROM PROVEEDOR_{self.id_oficina} WHERE ID_PROVEEDOR = ?"
        try:
            self.cursor.execute(query, (id_proveedor))
            self.conn.commit()
            super().closeConn()
            return True
        except Exception as ex:
            print(f"Error capturado: {ex}")
            super().closeConn()
            return False


class OficinaDAC(Conexion):
    def getAll(self):
        super().initConn()
        result = []
        query = f"SELECT * FROM OFICINA"
        self.cursor.execute(query)
        for row in self.cursor.fetchall():
            item = {
                'id_oficina': row[0],
                'nombre_of': row[1],
                'ubicacion': row[2]
            }
            result.append(item)
        super().closeConn()
        return result

    def getById(self, id_oficina):
        super().initConn()
        result = []
        query = f"SELECT * FROM OFICINA WHERE ID_OFICINA = ?"
        self.cursor.execute(query, id_oficina)
        row = self.cursor.fetchone()
        super().closeConn()
        if row:
            result.append({
                'id_oficina': row[0],
                'nombre_of': row[1],
                'ubicacion': row[2]
            })
            return result
        return None

    def add(self, item):
        super().initConn()
        query = f"""INSERT INTO OFICINA 
                   (ID_OFICINA, NOMBRE_OF, UBICACION) 
                   VALUES (?, ?, ?)"""
        try:
            self.cursor.execute(
                query,
                item['id_oficina'],
                item['nombre_of'],
                item['ubicacion']
            )
            self.conn.commit()
            super().closeConn()
            return True
        except Exception as ex:
            print(f"Error capturado: {ex}")
            super().closeConn()
            return False

    def update(self, item):
        super().initConn()
        query = f"""UPDATE OFICINA 
                   SET NOMBRE_OF = ?, UBICACION = ? 
                   WHERE ID_OFICINA = ?"""
        try:
            self.cursor.execute(
                query,
                item['nombre_of'],
                item['ubicacion'],
                item['id_oficina']
            )
            self.conn.commit()
            super().closeConn()
            return True
        except Exception as ex:
            print(f"Error capturado: {ex}")
            super().closeConn()
            return False

    def delete(self, id_oficina):
        super().initConn()
        query = f"DELETE FROM OFICINA WHERE ID_OFICINA = ?"
        try:
            self.cursor.execute(query, (id_oficina))
            self.conn.commit()
            super().closeConn()
            return True
        except Exception as ex:
            print(f"Error capturado: {ex}")
            super().closeConn()
            return False





if __name__ == "__main__":         
    db = ProveedorDAC()
    # item = {'id_servicio':'SERV007', 'id_oficina':'{self.id_oficina}', 'id_proveedor':'PROV002' , 'descripcion_ser':'Nuevo Servicio', 'precio_ser':790.5}
    # response = db.delete('SERV0{self.id_oficina}')
    # print(db.getAll())
    # if response:
    #     print("eliminado")
    # else:
        # print('error')
    result = db.getById('PROV001')
    print(result)
    for row in result:
        print(row)