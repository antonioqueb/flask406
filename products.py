import sqlite3

# Definimos una constante para la segunda base de datos
DATABASE_PRODUCTS = 'products.db'

# Función para conectar con la base de datos de productos
def get_db_connection_products():
    conn = sqlite3.connect(DATABASE_PRODUCTS)
    conn.row_factory = sqlite3.Row
    return conn

# Función para configurar la base de datos de productos y crear la tabla si no existe
def setup_database_products():
    conn = get_db_connection_products()
    conn.execute('''
    CREATE TABLE IF NOT EXISTS products (
        product_id INTEGER PRIMARY KEY AUTOINCREMENT,
        product_name TEXT NOT NULL,
        price REAL NOT NULL
    );
    ''')
    conn.commit()
    conn.close()

# Bloque principal que ejecuta la configuración inicial de la base de datos de productos
if __name__ == '__main__':
    setup_database_products()
