import token

import mysql.connector
import hashlib

from dataclasses import dataclass, asdict
from flask import jsonify
from time import time



class UserDAO:

    def connectBBDD(self):
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="Tapatapp"
        )
        return connection
   
    def login(self, identifier, password):
        # conexio a la base de dades
        con=self.connectBBDD()
        cursor=con.cursor(dictionary=True)
        query = """
        SELECT * FROM User WHERE (username = %s OR email = %s) AND password = %s
    """    
        cursor.execute(query, (identifier, identifier, password))
        user = cursor.fetchone()
        if user:
            token = self.setTokenUser(user['username'])
            user['token'] = token
        cursor.close()
        con.close()
        # Query per a validar usuari i contrasenya
        
        # Si validacio ok, generar token i actualitzar usuari a la base de dades
            # Si torna 1 registre User ok
            # Si no none 
        # Tancar connexio
        return user
    
    def setTokenUser(self, username):
        # conexio a la base de dades
        con=self.connectBBDD()
        cursor = con.cursor(dictionary=True)
        # Query per a generar token i actualitzar usuari a la base de dades
        token = self.getHash(username)
        query = "UPDATE User SET token = '" + token + "' WHERE username = '" + username + "'"
        cursor.execute(query)
        con.commit()
        # Tancar connexio
        cursor.close()
        con.close()
        return token


    def getHash(self, username):
        milliseconds = str(time() * 1000)
        data = username + milliseconds
        hash_object = hashlib.sha256(data.encode('utf-8'))
        return hash_object.hexdigest()
        
dao = UserDAO()
print(dao.getHash("mare"))
u = dao.login("mare", "mare")
print(u)

