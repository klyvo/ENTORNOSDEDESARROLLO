from dadesServer import *
from dataclasses import dataclass, asdict
from flask import jsonify




class UserDAO:
    def __init__(self):
        self.users = users

    def getAllUsers(self):
        return [user.__dict__ for user in self.users]

    def getUserByUsername(self, username):
        for user in self.users:
            if user.username == username:
                return user.__dict__
        return None
    
    def login(self, identifier, password):
        for user in self.users:
            if (user.username == identifier or user.email == identifier) and user.password == password:
                return user
        return None
    
    def getUserRole(self,user_id):
        return [relation['rol_id'] for relation in relation_user_child if relation['user_id'] == user_id]




#####################################################
#  Test / Proves Codi per veure funcionament 
#  (comentar quan s'ha testejat)
#####################################################

## print All Users from list dadesServer: 
#print(" ".join([str(x) for x in users]))
## print All Users from DAO
''' 
userDao = UserDAO()
listAllUsers=userDao.getAllUsers()
print(type(listAllUsers))
print(" ".join([str(x) for x in userDao.getAllUsers()]))


@dataclass
class ApiResponse():
    msg: str
    coderesponse: str
    data: list

response = ApiResponse(
    msg="All Users",
    coderesponse="1",
    data=userDao.getAllUsers()
)
print(response)
print(asdict(response))
Vol dir que estàs cridant jsonify() fora d’una ruta Flask o fora del context de l’aplicació.
jsonify() només pot usar-se quan Flask té un app context actiu, és a dir:
dins d’una funció decorada amb @app.route
o dins d’un with app.app_context():
'''
#print(jsonify(asdict(response)))