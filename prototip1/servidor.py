from flask import Flask, jsonify, request 

class User:
    def __init__(self,username, nom, password, email, rol="tutor"):
        self.username=username
        self.nom=nom
        self.password=password
        self.email=email
        self.rol=rol
    
    def __str__(self):
        return self.nom

#us1=User(username="ama",nom="Rob Halford",password="12345", email="rob@gmail.com",rol="tutor")
#print(us1)
users = [
    User(username="rob",nom="Rob Halford",password="12345", email="rob@gmail.com",rol="tutor"),
    User(username="john",nom="John Cannigan",password="12345", email="john@gmail.com",rol="tutor"),
    User(username="maria",nom="Maria Sams",password="12345", email="maria@gmail.com",rol="admin")
]


class UserDao:
    def __init__(self):
        self.users=users
    
    def getUserByUsername(self,uname):
        user = None
        for u in self.users:
            if u.username == uname:
                user = u.__dict__
        return user

    def getAllUsers(self):
        resposta = []
        for u in self.users:
            resposta.append(u.__dict__)
        return resposta

# Test DAO
'''user_dao = UserDao()
response=user_dao.getUserByUsername("maria")
print(response)
response=user_dao.getUserByUsername("AAAA")
print(response) '''
# End TEST

# Instanciem el Dao User
user_dao = UserDao()

app = Flask(__name__)

@app.route('/user',methods=['GET'])
def user():
    resposta=""
    username = request.args.get("username",default="")
    if username != "":
        resposta=user_dao.getUserByUsername(username)
        if resposta == None:
            resposta = {"msg":"Usuari No trobat"}
    else:
        resposta = {"msg":"Falta paràmetre Username"}
    
    return jsonify(resposta)


@app.route('/getuser', methods=['GET'])
def getuser():
    resposta = user_dao.getAllUsers()
    return jsonify(resposta)

if __name__ == '__main__':
    app.run(debug=True)
