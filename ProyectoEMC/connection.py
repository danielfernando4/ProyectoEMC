import pyodbc
try:
    # Configurar la conexión
    conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=(localdb)\ServidorDB;DATABASE=dbfool;UID=admin;PWD=admin')

    # Crear un cursor para ejecutar consultas
    cursor = conn.cursor()

    # Ejecutar una consulta
    cursor.execute("SELECT * FROM cliente")

    # Obtener resultados
    rows = cursor.fetchall()
    for row in rows:
        print(row)

except Exception as ex:
    print(ex)
    
finally:
    cursor.close()
    conn.close()
    print("Conexión finalizada")


