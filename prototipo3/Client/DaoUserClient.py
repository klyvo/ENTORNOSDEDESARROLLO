import requests

class DaoUserClient:
    def __init__(self, base_url="http://127.0.0.1:5000"):
        self.base_url = base_url
        self.token = None

    def login(self, username, password):
        """
        Primer paso: Intercambia credenciales por un token.
        Basado en el flujo del diagrama de secuencia.
        """
        url = f"{self.base_url}/login"
        payload = {
            "username": username,
            "password": password
        }
        
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.token = data['token'] # Guardamos el token para futuras peticiones
                print(f"✅ Login exitoso. Token obtenido.")
                return self.token
            else:
                print(f"❌ Error en login: {response.status_code}")
                return None
        except Exception as e:
            print(f"⚠️ Error de conexión: {e}")
            return None

    def get_childs_with_token(self, token_to_use=None):
        """
        Segundo paso: Realiza peticiones usando SOLO el token.
        Tal como dibujaste en la pizarra: /getChilds enviando TokenA.
        """
        # Si no pasamos un token por parámetro, usamos el que tengamos guardado
        tk = token_to_use if token_to_use else self.token
        
        if not tk:
            print("🚫 No hay token disponible. Debes hacer login primero.")
            return None

        url = f"{self.base_url}/getChilds"
        # Enviamos el token en el Header como 'TokenUser' (según tu diagrama)
        headers = {
            "TokenUser": tk
        }

        try:
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                return response.json().get('childs', [])
            else:
                print(f"❌ Error de autenticación/datos: {response.status_code}")
                return None
        except Exception as e:
            print(f"⚠️ Error de conexión: {e}")
            return None

# --- EJEMPLO DE USO (Prueba en terminal) ---
if __name__ == "__main__":
    client = DaoUserClient()
    
    # 1. Login inicial para conseguir el token
    mi_token = client.login("mare", "mare")
    
    if mi_token:
        print(f"Mi Token actual es: {mi_token}")
        
        # 2. A partir de aquí, ya podemos trabajar SOLO con el token
        print("\nSolicitando lista de hijos usando solo el token...")
        hijos = client.get_childs_with_token(mi_token)
        
        if hijos:
            for hijo in hijos:
                print(f"👶 Niño encontrado: {hijo['child_name']} (Sueño medio: {hijo['sleep_average']}h)")