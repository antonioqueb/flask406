import sqlite3

def get_db_connection():
    # Establece una conexión con la base de datos principal 'users.db'.
    conn = sqlite3.connect('users.db')
    
    # Adjunta una segunda base de datos llamada 'products.db' al mismo entorno de conexión.
    # Esto permite realizar consultas que incluyan tablas de ambas bases de datos.
    conn.execute('ATTACH DATABASE "products.db" AS products_db')
    
    # Retorna el objeto de conexión configurado.
    return conn

def join_users_products():
    # Obtiene una conexión a la base de datos que incluye tanto 'users.db' como 'products.db'.
    conn = get_db_connection()
    
    # Define un query SQL que realiza un JOIN entre la tabla 'users' en la base de datos principal
    # y la tabla 'products' en la base de datos adjunta 'products_db'.
    # El JOIN se realiza sobre la coincidencia de 'product_id' en 'products' con 'id' en 'users'.
    query = '''
    SELECT u.name, u.email, p.product_name, p.price
    FROM users u
    INNER JOIN products_db.products p ON p.product_id = u.id
    '''
    
    # Ejecuta el query y recoge todos los resultados en una lista.
    results = conn.execute(query).fetchall()
    
    # Cierra la conexión a la base de datos una vez que los datos han sido obtenidos.
    conn.close()
    
    # Retorna los resultados del query.
    return results

if __name__ == '__main__':
    # Si el script se ejecuta como programa principal, llama a la función 'join_users_products'
    # y luego imprime cada resultado.
    results = join_users_products()
    for result in results:
        print(result['name'], result['email'], result['product_name'], result['price'])
