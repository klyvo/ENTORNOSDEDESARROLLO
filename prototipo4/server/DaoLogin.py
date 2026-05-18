import mysql.connector
import hashlib
from time import time


class DaoLogin:
    """DAO per a les operacions de Login amb la base de dades"""

    def connectBBDD(self):
        """Connecta a la base de dades MySQL"""
        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="root",
                database="Tapatapp"
            )
            return connection
        except mysql.connector.Error as err:
            print(f"Error de conexió a la base de dades: {err}")
            return None

    def login(self, identifier, password):
        """
        Login amb username o email i password
        Retorna l'usuari si és validat, None si no
        """
        con = self.connectBBDD()
        if not con:
            return None
        
        try:
            cursor = con.cursor(dictionary=True)
            query = """
                SELECT u.id, u.username, u.password, u.email, u.token,
                       ruc.rol_id as idrole
                FROM User u
                LEFT JOIN RelationUserChild ruc ON u.id = ruc.user_id
                WHERE (u.username = %s OR u.email = %s) AND u.password = %s
                LIMIT 1
            """
            cursor.execute(query, (identifier, identifier, password))
            user = cursor.fetchone()
            
            if user:
                # Si no té rol assignat, assignem 1 (Admin)
                if user['idrole'] is None:
                    user['idrole'] = 1
                
                # Generar token
                token = self.getHash(user['username'])
                self.setTokenUser(user['username'], token)
                user['token'] = token
            
            cursor.close()
            return user
        except mysql.connector.Error as err:
            print(f"Error en la consulta de login: {err}")
            return None
        finally:
            con.close()

    def loginByToken(self, token):
        """
        Validació de login per token
        Retorna les dades de l'usuari si el token és valid, None si no
        """
        con = self.connectBBDD()
        if not con:
            return None
        
        try:
            cursor = con.cursor(dictionary=True)
            query = """
                SELECT u.id, u.username, u.email, u.token,
                       ruc.rol_id as idrole
                FROM User u
                LEFT JOIN RelationUserChild ruc ON u.id = ruc.user_id
                WHERE u.token = %s
                LIMIT 1
            """
            cursor.execute(query, (token,))
            user = cursor.fetchone()
            
            if user:
                # Si no té rol assignat, assignem 1 (Admin)
                if user['idrole'] is None:
                    user['idrole'] = 1
            
            cursor.close()
            return user
        except mysql.connector.Error as err:
            print(f"Error en la validació del token: {err}")
            return None
        finally:
            con.close()

    def setTokenUser(self, username, token):
        """Actualitza el token de l'usuari a la base de dades"""
        con = self.connectBBDD()
        if not con:
            return False
        
        try:
            cursor = con.cursor()
            query = "UPDATE User SET token = %s WHERE username = %s"
            cursor.execute(query, (token, username))
            con.commit()
            cursor.close()
            return True
        except mysql.connector.Error as err:
            print(f"Error actualizando token: {err}")
            return False
        finally:
            con.close()

    def getHash(self, username):
        """Genera un hash SHA256 per al token basant-se en username i timestamp"""
        milliseconds = str(time() * 1000)
        data = username + milliseconds
        hash_object = hashlib.sha256(data.encode('utf-8'))
        return hash_object.hexdigest()
