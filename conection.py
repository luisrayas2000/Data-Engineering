import mysql.connector

# Conectar a la base de datos
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",  # si no tienes contraseña
    database="base_prueba"
)

# Verificar la conexión
if conn.is_connected():
    print("Conectado exitosamente a la base de datos")

# Cerrar la conexión
#conn.close()

cursor = conn.cursor()

create_table_query = """
CREATE TABLE IF NOT EXISTS clientes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100),
    email VARCHAR(100)
);
"""

# Ejecutar la consulta
cursor.execute(create_table_query)

# Confirmar la creación
print("Tabla creada exitosamente")

# SQL para insertar datos en la tabla
insert_query = """
INSERT INTO clientes (nombre, email) 
VALUES (%s, %s)
"""

# Datos a insertar
data = ("Juan Pérez", "juan.perez@email.com")

# Ejecutar la consulta

cursor.execute(insert_query, data)

# Confirmar los cambios en la base de datos
conn.commit()

print("Datos insertados exitosamente")


# SQL para seleccionar todos los registros de la tabla
select_query = "SELECT * FROM clientes"

# Ejecutar la consulta
cursor.execute(select_query)

# Obtener los resultados
result = cursor.fetchall()

# Mostrar los resultados
for row in result:
    print(row)
