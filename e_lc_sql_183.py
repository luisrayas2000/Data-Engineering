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
    CREATE TABLE IF NOT EXISTS costumers (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100)
    );
    """

    # Crear la tabla (si no existe)
    create_table_query_2 = """
    CREATE TABLE IF NOT EXISTS orders (
        id INT AUTO_INCREMENT PRIMARY KEY,
        costumerId INT,
        FOREIGN KEY (costumerId) REFERENCES costumers ON DELETE CASCADE ON UPDATE CASCADE
    );
    """
    cursor.execute(create_table_query)
    print("Tabla creada exitosamente")
    cursor.execute(create_table_query_2)
    print("Tabla creada exitosamente")
    # Insertar datos
    insert_query = """
    INSERT INTO costumers (name)  
    VALUES (%s)
    """

    insert_query_2 = """
    INSERT INTO orders (costumerId)  
    VALUES (%s)
    """

    # Lista de datos a insertar
    data = [
        ("Joe",),
        ("Henry",),
        ("Sam",),
        ("Max",),
        # Puedes agregar más tuplas aquí
    ]

    data_2 = [
        (3,),
        (1,),
        # Puedes agregar más tuplas aquí
    ]

    # Insertar múltiples registros
    cursor.executemany(insert_query, data)
    conn.commit()
    print(f"{cursor.rowcount} datos insertados exitosamente")


    cursor.executemany(insert_query_2, data_2)
    conn.commit()
    print(f"{cursor.rowcount} datos insertados exitosamente en la segunda tabla")
    # Seleccionar datos
    select_query = "SELECT * FROM costumers"
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