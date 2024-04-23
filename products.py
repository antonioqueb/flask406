import sqlite3

# Definimos una constante para la base de datos de productos
DATABASE_PRODUCTS = 'products.db'

# Función para conectar con la base de datos de productos
def get_db_connection_products():
    conn = sqlite3.connect(DATABASE_PRODUCTS)
    conn.row_factory = sqlite3.Row
    return conn

# Función para agregar un producto a la base de datos
def add_product(product_name, price, user_id):
    conn = get_db_connection_products()
    conn.execute('INSERT INTO products (product_name, price, user_id) VALUES (?, ?, ?)', (product_name, price, user_id))
    conn.commit()
    conn.close()

# Función para obtener todos los productos de la base de datos
def get_all_products():
    conn = get_db_connection_products()
    products = conn.execute('SELECT * FROM products').fetchall()
    conn.close()
    return products

# Función para configurar la base de datos de productos y crear la tabla si no existe
# En el archivo products.py

# En el archivo products.py

# Función para configurar la base de datos de productos y crear la tabla si no existe
def setup_database_products():
    conn = get_db_connection_products()
    conn.execute('''
    CREATE TABLE IF NOT EXISTS products (
        product_id INTEGER PRIMARY KEY AUTOINCREMENT,
        product_name TEXT NOT NULL,
        price REAL NOT NULL,
        user_id INTEGER,  -- Agrega la columna user_id a la tabla
        FOREIGN KEY (user_id) REFERENCES users(id)  -- Define una clave foránea para relacionar los productos con los usuarios
    );
    ''')
    conn.commit()
    conn.close()

# Bloque principal que ejecuta la configuración inicial de la base de datos de productos
if __name__ == '__main__':
    setup_database_products()
