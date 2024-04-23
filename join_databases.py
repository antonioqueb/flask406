import sqlite3

def get_db_connection():
    conn = sqlite3.connect('users.db')  # Conexión principal
    conn.execute('ATTACH DATABASE "products.db" AS products_db')  # Adjunta la segunda base de datos
    return conn

# Ejemplo de función para realizar una consulta que une datos de ambas bases de datos
def join_users_products():
    conn = get_db_connection()
    query = '''
    SELECT u.name, u.email, p.product_name, p.price
    FROM users u
    INNER JOIN products_db.products p ON p.product_id = u.id  # Suponiendo que 'id' de users corresponda a 'product_id' en products
    '''
    results = conn.execute(query).fetchall()
    conn.close()
    return results

if __name__ == '__main__':
    results = join_users_products()
    for result in results:
        print(result['name'], result['email'], result['product_name'], result['price'])
