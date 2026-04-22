from flask import Flask, request, jsonify
from DaoServer import UserDAO

app = Flask(__name__)
dao = UserDAO()

@app.route('/login', methods=['POST'])
def login():
    # Obtenemos los datos del JSON enviado por el cliente
    data = request.get_json()
    identifier = data.get('username') # Puede ser username o email según tu DAO
    password = data.get('password')

    if not identifier or not password:
        return jsonify({"error": "Missing credentials"}), 400

    # Usamos el método login de tu UserDAO
    user = dao.login(identifier, password)

    if user:
        # Si el login es OK, devolvemos la info del usuario con el Token generado
        return jsonify({
            "status": "success",
            "user": {
                "id": user['id'],
                "username": user['username'],
                "email": user['email'],
                "token": user['token']
            }
        }), 200
    else:
        return jsonify({"error": "Invalid username or password"}), 401

@app.route('/getChilds', methods=['GET'])
def get_childs():
    # Según tu diagrama, el token viene en el header
    token = request.headers.get('TokenUser')
    
    if not token:
        return jsonify({"error": "No token provided"}), 401

    # Validamos el token buscando al usuario en la BBDD
    con = dao.connectBBDD()
    cursor = con.cursor(dictionary=True)
    
    # Query para buscar el usuario por token y obtener sus hijos relacionados
    query = """
        SELECT c.* FROM Child c
        JOIN RelationUserChild ruc ON c.id = ruc.child_id
        JOIN User u ON ruc.user_id = u.id
        WHERE u.token = %s
    """
    cursor.execute(query, (token,))
    childs = cursor.fetchall()
    
    cursor.close()
    con.close()

    if childs:
        return jsonify({"status": "success", "childs": childs}), 200
    else:
        # Si no hay hijos o el token no es válido
        return jsonify({"error": "Authenticated Service / No childs found"}), 403

if __name__ == '__main__':
    # Ejecutamos el servidor en el puerto 5000
    app.run(debug=True, port=5000)