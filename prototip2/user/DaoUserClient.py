import requests
from user import User
from user import *
from flask import Flask, request, jsonify


class daoUserClient:
    base_url = "http://localhost:5000"

    def login(self, user):
        # user.username
        # user.password
        # Agafo username i password del objecte user
        # Peticio http al Webservice
        URL_peticio = self.base_url + "/login"
        params_post = {
            "username": user.username,
            "password": user.password
        }
        response = requests.post(URL_peticio, json=params_post)
        if response.status_code == 200:
            user_data_raw = response.json()
            code_response = user_data_raw["coderesponse"]
            if code_response == "1":
                user = User(user_data_raw['id'], user_data_raw['username']
                , "",user_data_raw['email']
                , user_data_raw['idrole'], user_data_raw['token'])
                return user
        
            else:
                return None
        else:
            return None

    def DaoChild(self, user):
        """
        Obtiene los hijos asociados a un usuario usando el endpoint /child del servidor.
        user: instancia de User (debe tener id y token)
        Devuelve la lista de hijos o None si hay error.
        """
        URL_peticio = self.base_url + "/child"
        headers = {"Authorization": user.token} if user.token else {}
        params_post = {"iduser": user.id}
        response = requests.post(URL_peticio, json=params_post, headers=headers)
        if response.status_code == 200:
            data = response.json()
            return data.get("children", [])
        else:
            return None
