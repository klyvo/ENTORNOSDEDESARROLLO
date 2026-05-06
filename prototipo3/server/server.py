from flask import Flask, request, jsonify
from DaoServer import UserDAO
from dataclasses import asdict # Asegúrate de tener esto para el ApiResponse

app = Flask(__name__)
dao = UserDAO()

@app.route('/login', methods=['POST'])
def login():
    # 1. Intentamos obtener el Token del header primero
    token = request.headers.get("api-token")
    user = None

    if token:
        # Intentamos buscar al usuario por ese token
        user = dao.getUserByToken(token)
    
    # 2. Si no hay token o el token no es válido, intentamos login por Body (JSON)
    if not user:
        data = request.get_json()
        if data:
            identifier = data.get('username')
            password = data.get('password')
            
            if identifier and password:
                user = dao.login(identifier, password)

    # 3. Respuesta final según si encontramos al usuario o no
    if user:
        return jsonify({
            "status": "success",
            "message": "Authenticated",
            "user": {
                "id": user['id'],
                "username": user['username'],
                "email": user['email'],
                "token": user['token']
            }
        }), 200
    else:
        # Si llegamos aquí es que falló el Token Y fallaron las credenciales
        return jsonify({
            "status": "error",
            "message": "Access not Granted / Invalid Credentials"
        }), 401

@app.route('/getChilds', methods=['GET'])
def get_childs():
    # Usamos el mismo nombre de header para ser consistentes
    token = request.headers.get('api-token')
    
    if not token:
        return jsonify({"error": "No token provided"}), 401

    con = dao.connectBBDD()
    cursor = con.cursor(dictionary=True)
    
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
    return jsonify({"error": "No childs found for this user"}), 404

if __name__ == '__main__':
    app.run(debug=True, port=5000)