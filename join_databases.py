import sqlite3

def get_db_connection():
    conn = sqlite3.connect('users.db')  # Conexión principal
    conn.execute('ATTACH DATABASE "products.db" AS products_db')  # Adjunta la segunda base de datos
    return conn

def join_users_products():
    conn = get_db_connection()
    # Query que une datos de las tablas users y products a través de sus respectivos IDs
    query = '''
    SELECT u.name, u.email, p.product_name, p.price
    FROM users u
    INNER JOIN products_db.products p ON p.product_id = u.id
    '''
    results = conn.execute(query).fetchall()
    conn.close()
    return results

if __name__ == '__main__':
    results = join_users_products()
    for result in results:
        print(result['name'], result['email'], result['product_name'], result['price'])
