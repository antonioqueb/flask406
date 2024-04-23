# app.py
# Importar las funciones y clases necesarias de Flask y otros módulos
from flask import Flask, render_template, request, redirect, url_for
import database as db  # Importar el módulo de base de datos personalizado
import products as pdb
# Importar las funciones necesarias desde el módulo users.py


# Crear una instancia de la aplicación Flask
app = Flask(__name__)

# Decorador que define la ruta principal '/' y vincula la función 'home' a esta ruta
@app.route('/')
def home():
    users = db.get_all_users()
    products = pdb.get_all_products()  # Obtener todos los productos
    return render_template('home.html', users=users, products=products)

# Decorador que define la ruta '/add' y permite métodos HTTP GET y POST
@app.route('/add', methods=['GET', 'POST'])
def add_user():
    """Agrega un nuevo usuario a la base de datos."""
    if request.method == 'POST':  # Verificar si la solicitud es POST
        name = request.form['name']  # Obtener el nombre del formulario
        email = request.form['email']  # Obtener el email del formulario
        db.add_user(name, email)  # Añadir el nuevo usuario a la base de datos
        return redirect(url_for('home'))  # Redireccionar a la página principal
    return render_template('add_user.html')  # Renderizar el formulario para agregar usuario si no es POST

# Decorador que define la ruta '/edit/<int:id>' y permite métodos HTTP GET y POST
@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_user(id):
    """Edita un usuario existente."""
    user = db.get_user_by_id(id)  # Obtener el usuario por ID
    if request.method == 'POST':  # Verificar si la solicitud es POST
        name = request.form['name']  # Obtener el nuevo nombre del formulario
        email = request.form['email']  # Obtener el nuevo email del formulario
        db.update_user(id, name, email)  # Actualizar los datos del usuario en la base de datos
        return redirect(url_for('home'))  # Redireccionar a la página principal
    return render_template('edit_user.html', user=user)  # Renderizar el formulario de edición con los datos del usuario

# Decorador que define la ruta '/delete/<int:id>' y permite el método HTTP GET
@app.route('/delete/<int:id>', methods=['GET'])
def delete_user(id):
    """Elimina un usuario."""
    db.delete_user(id)  # Eliminar el usuario por ID de la base de datos
    return redirect(url_for('home'))  # Redireccionar a la página principal


@app.route('/add_product', methods=['GET', 'POST'])
def add_product():
    """Agrega un nuevo producto a la base de datos."""
    users = db.get_all_users()  # Obtener todos los usuarios
    if request.method == 'POST':
        product_name = request.form['product_name']
        price = request.form['price']
        user_id = request.form['user_id']  # Obtener el ID del usuario seleccionado
        pdb.add_product(product_name, float(price), user_id)  # Asegúrate de pasar el ID del usuario al agregar el producto
        return redirect(url_for('home'))
    return render_template('add_product.html', users=users)  # Pasar la lista de usuarios a la plantilla


# Define la ruta para ver los productos de un usuario
@app.route('/view_products/<int:user_id>')
def view_products(user_id):
    user = get_user_by_id(user_id)  # Obtiene el usuario por su ID
    products = get_products_by_user_id(user_id)  # Obtiene los productos del usuario por su ID
    return render_template('view_products.html', user=user, products=products)



# Punto de entrada del script, verifica si este archivo es el ejecutado directamente
if __name__ == '__main__':
    app.run(debug=True)  # Ejecutar la aplicación con el modo de depuración activado
