from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/user', methods=['GET'])
def user():
    # Parameter
    resposta=""
    username = request.args.get("username", default="")
    # Si els parametres OK
    if username !="":
    # Anar al DAO Server i cercar User per username
    # respondre amb dades Usuari si trobat
        resposta ="username = " + username
    else:
    # Si els parametres NO ok
    # respondre error
        resposta = "username NO informat"
    return resposta

if __name__ == '__main__':
    app.run(debug=True)