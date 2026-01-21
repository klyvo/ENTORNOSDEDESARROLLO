from flask import Flask, jsonify
import requests
class User:
    def __init__(self, username, nom, password, email, rol="tutor"):
        self.username=username
        self.nom=nom
        self.password=password
        self.email=email
        self.rol=rol
    
    def __str__(self):
        return self.nom
    
class daoUserClient:
    def getUserByUsername(self, username):
        #Petició Http al Webservice
        response = requests.get('http://localhost:5000/user?username='+username)

        #Si la petició OK = code response 200
        if response.status_code == 200:
            #Obtenemos json
            user_data_raw = response.json()

            #Crear objeto user si se encontro
            if 'msg' in user_data_raw.keys():
                return None
            
            #Si no ha trobat return None
            else:
                user=User(user_data_raw['username'],user_data_raw['nom'],
                          user_data_raw['password'],user_data_raw['email'],user_data_raw['rol'])
                return user
        
        return None
    
class ViewConsole:
    def getInputUsername():
        #TODO
        return None
    
    def showUserInfo(data):
        #TODO
        return None
    
user_daoClient = daoUserClient()
a=user_daoClient.getUserByUsername("rob")
print(a.nom,a.email,a.rol)
a=user_daoClient.getUserByUsername("robdsadasdasd")
print(a)