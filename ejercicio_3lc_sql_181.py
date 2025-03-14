import mysql.connector

try:
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

    cursor = conn.cursor()

    # Crear la tabla (si no existe)
    create_table_query = """
    CREATE TABLE IF NOT EXISTS employee (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100),
        salary INT,
        managerId INT
    );
    """
    cursor.execute(create_table_query)
    print("Tabla creada exitosamente")

    # Insertar datos
    insert_query = """
    INSERT INTO employee (name, salary, managerId)  
    VALUES (%s,%s,%s)
    """

    # Lista de datos a insertar
    data = [
        ("pancho",70000,2),
        ("pedro",50000,1),
        # Puedes agregar más tuplas aquí
    ]

    # Insertar múltiples registros
    cursor.executemany(insert_query, data)
    conn.commit()
    print(f"{cursor.rowcount} datos insertados exitosamente")

    # Seleccionar datos
    select_query = "SELECT * FROM employee"
    cursor.execute(select_query)
    result = cursor.fetchall()
    for row in result:
        print(row)

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    # Cerrar cursor y conexión
    if 'cursor' in locals():
        cursor.close()
    if 'conn' in locals() and conn.is_connected():
        conn.close()
        print("Conexión cerrada")