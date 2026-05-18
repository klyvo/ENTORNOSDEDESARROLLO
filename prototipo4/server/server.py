from flask import Flask, request, jsonify
from DaoLogin import DaoLogin
import json

app = Flask(__name__)
dao = DaoLogin()


@app.route('/login', methods=['POST'])
def login():
    """
    Endpoint de Login amb username/email i password
    
    Paràmetres esperats (JSON):
    - username: string (username o email)
    - password: string (password de l'usuari)
    
    Resposta si és validat (200):
    {
        "coderesponse": "1",
        "data": {
            "email": "prova@gmail.com",
            "id": 1,
            "idrole": 1,
            "password": "12345",
            "token": "...",
            "username": "mare"
        },
        "msg": "Authenticated"
    }
    
    Resposta si NO és validat (400):
    {
        "coderesponse": "0",
        "msg": "No validat"
    }
    """
    try:
        data = request.get_json()
        
        # Validar que els paràmetres requerits existeixen
        if not data or 'username' not in data or 'password' not in data:
            return jsonify({
                "coderesponse": "0",
                "msg": "Paràmetres requerits no proporcionats"
            }), 400
        
        username = data.get('username')
        password = data.get('password')
        
        # Validar al DAO
        user = dao.login(username, password)
        
        if user:
            # Login exitós
            response = {
                "coderesponse": "1",
                "data": {
                    "email": user['email'],
                    "id": user['id'],
                    "idrole": user['idrole'],
                    "password": user['password'],
                    "token": user['token'],
                    "username": user['username']
                },
                "msg": "Authenticated"
            }
            return jsonify(response), 200
        else:
            # Login fallat
            response = {
                "coderesponse": "0",
                "msg": "No validat"
            }
            return jsonify(response), 400
    
    except Exception as e:
        print(f"Error en l'endpoint /login: {str(e)}")
        return jsonify({
            "coderesponse": "0",
            "msg": f"Error del servidor: {str(e)}"
        }), 500


@app.route('/login/token', methods=['POST'])
def login_token():
    """
    Endpoint de validació de login per token
    
    Paràmetres esperats (Header):
    - Authorization: string (token)
    
    Resposta si és validat (200):
    {
        "id": 1,
        "username": "mare",
        "email": "prova@gmail.com",
        "token": "token12345",
        "idrole": "2",
        "msg": "Usuari Ok",
        "coderesponse": "1"
    }
    
    Resposta si NO és validat (400):
    {
        "coderesponse": "0",
        "msg": "No validat"
    }
    """
    try:
        # Obtenir el token del header Authorization
        auth_header = request.headers.get('Authorization')
        
        if not auth_header:
            return jsonify({
                "coderesponse": "0",
                "msg": "No validat"
            }), 400
        
        # El token pot venir com "Bearer token" o directament el token
        token = auth_header.replace('Bearer ', '') if auth_header.startswith('Bearer ') else auth_header
        
        # Validar el token al DAO
        user = dao.loginByToken(token)
        
        if user:
            # Token válid
            response = {
                "id": user['id'],
                "username": user['username'],
                "email": user['email'],
                "token": user['token'],
                "idrole": str(user['idrole']),
                "msg": "Usuari Ok",
                "coderesponse": "1"
            }
            return jsonify(response), 200
        else:
            # Token inválid
            response = {
                "coderesponse": "0",
                "msg": "No validat"
            }
            return jsonify(response), 400
    
    except Exception as e:
        print(f"Error en l'endpoint /login/token: {str(e)}")
        return jsonify({
            "coderesponse": "0",
            "msg": f"Error del servidor: {str(e)}"
        }), 500


@app.route('/health', methods=['GET'])
def health():
    """Endpoint per verificar que el servidor és viu"""
    return jsonify({"status": "ok"}), 200


if __name__ == '__main__':
    # Executar el servidor en localhost:5000
    app.run(debug=True, host='localhost', port=5000)
