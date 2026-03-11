from flask import Flask, request, jsonify
from dadesServer import *
from DaoServer import *
import uuid

app = Flask(__name__)

user_dao = UserDao()
child_dao = ChildDao()
tap_dao = TapDao()
status_dao = StatusDao()
role_dao = RoleDao()
treatment_dao = TreatmentDao()


# Login

@app.route('/login', methods=['POST'])
def login():

    token_header = request.headers.get("Authorization")

    # Login por token
    if token_header:
        user = user_dao.getUserByToken(token_header)

        if user:
            return jsonify({
                "id": user.id,
                "username": user.username,
                "password": user.password,
                "email": user.email,
                "token": user.token,
                "idrole": user.idrole,
                "msg": "Usuari Ok",
                "coderesponse": "1"
            }), 200

        return jsonify({
            "coderesponse": "0",
            "msg": "No validat"
        }), 400


    # Login normal
    data = request.get_json()

    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({
            "coderesponse": "0",
            "msg": "No validat"
        }), 400

    user = user_dao.login(username, password)

    if user:
        # Para generar el token
        user.token = str(uuid.uuid4())

        return jsonify({
            "id": user.id,
            "username": user.username,
            "password": user.password,
            "email": user.email,
            "token": user.token,
            "idrole": user.idrole,
            "msg": "Usuari Ok",
            "coderesponse": "1"
        }), 200

    return jsonify({
        "coderesponse": "0",
        "msg": "No validat"
    }), 400


# Child

@app.route('/child', methods=['POST'])
def get_child():

    token = request.headers.get("Authorization")

    if not token:
        return jsonify({
            "coderesponse": "0",
            "msg": "No validat"
        }), 400

    user = user_dao.getUserByToken(token)

    if not user and not iduser.is_integer:
        return jsonify({
            "coderesponse": "0",
            "msg": "No validat"
        }), 400

    data = request.get_json()
    iduser = data.get("iduser")

    childs = child_dao.getChildrenByUser(iduser)

    return jsonify({
        "msg": str(len(childs)),
        "coderesponse": "1",
        "children": childs
    }), 200


if __name__ == '__main__':
    app.run(debug=True)