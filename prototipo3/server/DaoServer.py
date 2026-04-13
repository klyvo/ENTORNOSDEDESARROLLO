import mysql.connector

from dataclasses import dataclass, asdict
from flask import jsonify


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
        query = "SELECT * FROM User WHERE (username = %s OR email = %s) AND password = %s"

        cursor.execute(query, (identifier, identifier, password))
        user = cursor.fetchone()
        cursor.close()
        con.close()
        # Query per a validar usuari i contrasenya
        # Si validacio ok, generar token i actualitzar usuari a la base de dades
            # Si torna 1 registre User ok
            # Si no none 
        # Tancar connexio
        return user
    
dao = UserDAO()
u = dao.login("mare", "mare")
print(u)