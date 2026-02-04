from flask import Flask, jsonify, request

# --- 1. MODELOS DE DATOS (ADT) ---
class User:
    def __init__(self, id, username, nom, password, email, idrole, token):
        self.id = id
        self.username = username
        self.nom = nom
        self.password = password
        self.email = email
        self.idrole = idrole
        self.token = token

class Child:
    def __init__(self, id, child_name, sleep_average, treatment_id, time, parent_id):
        self.id = id
        self.child_name = child_name
        self.sleep_average = sleep_average
        self.treatment_id = treatment_id
        self.time = time
        self.parent_id = parent_id

# --- 2. CAPA DE ACCESO A DATOS (DAO) ---
class UserDao:
    def __init__(self):
        # Datos iniciales para pruebas
        self.users = [
            User(1, "mare", "Maria Sams", "12345", "prova@gmail.com", "2", "token12345"),
            User(2, "rob", "Rob Halford", "12345", "rob@gmail.com", "2", "token67890")
        ]
    
    def authenticate(self, username, password):
        for u in self.users:
            if (u.username == username or u.email == username) and u.password == password:
                return u
        return None

    def validate_by_token(self, token):
        for u in self.users:
            if u.token == token:
                return u
        return None

class ChildDao:
    def __init__(self):
        # Datos iniciales asociados a iduser=1 (mare)
        self.children = [
            Child(1, "Carol Child", 8, 1, 6, 1),
            Child(2, "Jaco Child", 10, 2, 6, 1)
        ]
    
    def get_children_by_parent(self, parent_id):
        # Filtramos la lista por el ID del usuario padre y devolvemos diccionarios
        return [c.__dict__ for c in self.children if c.parent_id == parent_id]

# --- 3. CONFIGURACIÓN E INSTANCIAS ---
app = Flask(__name__)
user_dao = UserDao()
child_dao = ChildDao()

# --- 4. ENDPOINTS (CONTROLADOR) ---

@app.route('/login', methods=['POST'])
def login():
    """Servicio de Login (por credenciales o por Token en Header)"""
    token_header = request.headers.get('Authorization')
    
    # Intento de login por Token
    if token_header:
        user = user_dao.validate_by_token(token_header)
    # Intento de login por JSON (username/password)
    else:
        data = request.get_json()
        if not data:
            return jsonify({"coderesponse": "0", "msg": "No validat"}), 400
        user = user_dao.authenticate(data.get('username'), data.get('password'))

    if user:
        return jsonify({
            "id": user.id,
            "username": user.username,
            "email": user.email,
            "token": user.token,
            "idrole": user.idrole,
            "msg": "Usuari Ok",
            "coderesponse": "1"
        }), 200
    else:
        return jsonify({"coderesponse": "0", "msg": "No validat"}), 400

@app.route('/child', methods=['POST'])
def get_children():
    """Servicio Child (Requiere Token en Header)"""
    token = request.headers.get('Authorization')
    user = user_dao.validate_by_token(token)
    
    if not user:
        return jsonify({"msg": "Token no vàlid", "coderesponse": "0"}), 401

    data = request.get_json()
    iduser = data.get('iduser')
    
    # Obtener lista de hijos desde el DAO
    lista_hijos = child_dao.get_children_by_parent(iduser)
    
    # Limpiar el campo parent_id para que el JSON coincida con tu diseño
    for h in lista_hijos:
        h.pop('parent_id', None)

    return jsonify({
        "msg": str(len(lista_hijos)),
        "coderesponse": "1",
        "data": lista_hijos # He añadido la clave 'data' para contener el array
    }), 200

if __name__ == '__main__':
    # Usamos el [Servidor de Desarrollo de Flask](https://flask.palletsprojects.com)
    app.run(debug=True, port=5000)
