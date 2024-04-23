# Importamos el módulo sqlite3 para trabajar con una base de datos SQLite
import sqlite3

# Definimos una constante que representa el nombre de nuestra base de datos
DATABASE = 'users.db'

# Función para conectar con la base de datos
def get_db_connection():
    conn = sqlite3.connect(DATABASE)  # Establecer conexión con la base de datos
    conn.row_factory = sqlite3.Row  # Configurar la conexión para que los registros se comporten como diccionarios
    return conn  # Devolver el objeto de conexión

# Función para obtener todos los usuarios de la base de datos
def get_all_users():
    conn = get_db_connection()  # Obtener conexión a la base de datos
    users = conn.execute('SELECT * FROM users').fetchall()  # Selecciona todos los campos de todos los registros en la tabla 'users'.
    conn.close()  # Cerrar la conexión con la base de datos
    return users  # Devolver la lista de usuarios

# Función para agregar un nuevo usuario a la base de datos
def add_user(name, email):
    conn = get_db_connection()  # Obtener conexión a la base de datos
    conn.execute('INSERT INTO users (name, email) VALUES (?, ?)', (name, email)) # Inserta un nuevo registro en la tabla 'users' con los valores especificados para 'name' y 'email'.
    conn.commit()  # Guardar los cambios en la base de datos
    conn.close()  # Cerrar la conexión

# Función para obtener un usuario por su ID
def get_user_by_id(user_id):
    conn = get_db_connection()  # Obtener conexión a la base de datos
    # Selecciona todos los campos de la tabla 'users' donde el campo 'id' coincide con 'user_id'.
    user = conn.execute('SELECT * FROM users WHERE id = ?', (user_id,)).fetchone()
    conn.close()  # Cerrar la conexión
    return user  # Devolver el usuario

# Función para actualizar los datos de un usuario
def update_user(user_id, name, email):
    conn = get_db_connection()  # Obtener conexión a la base de datos
    # Actualiza los valores de 'name' y 'email' en la tabla 'users' donde el campo 'id' coincide con 'user_id'.
    conn.execute('UPDATE users SET name = ?, email = ? WHERE id = ?', (name, email, user_id))
    conn.commit()  # Guardar los cambios en la base de datos
    conn.close()  # Cerrar la conexión

# Función para eliminar un usuario por su ID
def delete_user(user_id):
    conn = get_db_connection()  # Obtener conexión a la base de datos
    # Elimina el registro de la tabla 'users' donde el campo 'id' coincide con 'user_id'.
    conn.execute('DELETE FROM users WHERE id = ?', (user_id,))
    conn.commit()  # Guardar los cambios en la base de datos
    conn.close()  # Cerrar la conexión

# Función para configurar la base de datos y crear la tabla si no existe
def setup_database():
    conn = get_db_connection()  # Obtener conexión a la base de datos
    # Crea una nueva tabla llamada 'users' si no existe, con los campos 'id', 'name' y 'email'.
    conn.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE
    );
    ''')
    conn.commit()  # Guardar los cambios en la base de datos
    conn.close()  # Cerrar la conexión

# Bloque principal que ejecuta la configuración inicial de la base de datos
if __name__ == '__main__':
    setup_database()
