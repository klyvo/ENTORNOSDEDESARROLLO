import requests

class DaoUserClient:
    def __init__(self, base_url="http://127.0.0.1:5000"):
        self.base_url = base_url
        self.token = None

    def get_taps(self, token):
        url = f"{self.base_url}/taps"
        # Enviamos el token en los headers como vimos en ApiTester
        headers = {'api-token': token} 
        
        try:
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                return response.json().get('taps', [])
            else:
                print(f"Error: {response.status_code}")
                return []
        except Exception as e:
            print(f"Error de conexión: {e}")
            return []

    def login(self, username, password):
        """
        Login tradicional: Envía username y password.
        Recibe el objeto user y guarda el token.
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
                # En el Prototipo 3, el token está dentro de data['user']['token']
                self.token = data['user']['token']
                print(f"✅ Login exitoso. Token guardado.")
                return data # Devolvemos todo el dict para la View
            else:
                print(f"❌ Error en login: {response.status_code}")
                return None
        except Exception as e:
            print(f"⚠️ Error de conexión: {e}")
            return None

    def login_con_token(self, token_to_use=None):
        """
        Login por Token: Envía el token en el header al endpoint /login.
        """
        tk = token_to_use if token_to_use else self.token
        if not tk:
            print("🚫 No hay token disponible.")
            return None

        url = f"{self.base_url}/login"
        headers = {"api-token": tk}

        try:
            response = requests.post(url, headers=headers)
            if response.status_code == 200:
                print(f"✅ Re-autenticación por token exitosa.")
                return response.json()
            else:
                print(f"❌ Token inválido: {response.status_code}")
                return None
        except Exception as e:
            print(f"⚠️ Error de conexión: {e}")
            return None

    def get_childs(self, token_to_use=None):
        """
        Obtiene la lista de hijos usando el token en el header.
        """
        tk = token_to_use if token_to_use else self.token
        
        if not tk:
            print("🚫 No hay token disponible.")
            return None

        url = f"{self.base_url}/getChilds"
        headers = {"api-token": tk}

        try:
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                return response.json()
            else:
                print(f"❌ Error obteniendo hijos: {response.status_code}")
                return response.json() # Devolvemos el json con el error del server
        except Exception as e:
            print(f"⚠️ Error de conexión: {e}")
            return None

# --- EJEMPLO DE USO (Prueba en terminal) ---
if __name__ == "__main__":
    client = DaoUserClient()
    
    # 1. Prueba Login
    print("--- Probando Login ---")
    resultado = client.login("mare", "mare")
    
    if resultado:
        token = client.token
        print(f"Token obtenido: {token}")
        
        # 2. Prueba Get Childs
        print("\n--- Probando Get Childs ---")
        hijos_res = client.get_childs(token)
        if hijos_res and hijos_res.get('status') == 'success':
            for hijo in hijos_res['childs']:
                print(f"👶 Niño: {hijo['name']} | Edad: {hijo['age']}")