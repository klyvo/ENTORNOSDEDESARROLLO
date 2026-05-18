import requests
import json

# URL base del servidor Flask
BASE_URL = "http://localhost:5000"


def test_login():
    """Test del endpoint /login amb credentials"""
    print("=" * 50)
    print("Test: Login amb username i password")
    print("=" * 50)
    
    url = f"{BASE_URL}/login"
    headers = {'Content-Type': 'application/json'}
    data = {
        "username": "mare",
        "password": "mare"
    }
    
    try:
        response = requests.post(url, json=data, headers=headers)
        print(f"Status Code: {response.status_code}")
        print(f"Response: {json.dumps(response.json(), indent=2)}")
        
        if response.status_code == 200:
            token = response.json()['data']['token']
            return token
    except Exception as e:
        print(f"Error: {e}")
    
    return None


def test_login_invalid():
    """Test del endpoint /login amb credentials inválides"""
    print("\n" + "=" * 50)
    print("Test: Login amb credentials inválides")
    print("=" * 50)
    
    url = f"{BASE_URL}/login"
    headers = {'Content-Type': 'application/json'}
    data = {
        "username": "mare",
        "password": "contrasenya_incorrecta"
    }
    
    try:
        response = requests.post(url, json=data, headers=headers)
        print(f"Status Code: {response.status_code}")
        print(f"Response: {json.dumps(response.json(), indent=2)}")
    except Exception as e:
        print(f"Error: {e}")


def test_login_by_token(token):
    """Test del endpoint /login/token"""
    print("\n" + "=" * 50)
    print("Test: Login per token")
    print("=" * 50)
    
    url = f"{BASE_URL}/login/token"
    headers = {
        'Content-Type': 'application/json',
        'Authorization': token
    }
    
    try:
        response = requests.post(url, headers=headers)
        print(f"Status Code: {response.status_code}")
        print(f"Response: {json.dumps(response.json(), indent=2)}")
    except Exception as e:
        print(f"Error: {e}")


def test_login_by_invalid_token():
    """Test del endpoint /login/token amb token inválid"""
    print("\n" + "=" * 50)
    print("Test: Login per token inválid")
    print("=" * 50)
    
    url = f"{BASE_URL}/login/token"
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'token_invalid_xyz123'
    }
    
    try:
        response = requests.post(url, headers=headers)
        print(f"Status Code: {response.status_code}")
        print(f"Response: {json.dumps(response.json(), indent=2)}")
    except Exception as e:
        print(f"Error: {e}")


def test_health():
    """Test del endpoint /health"""
    print("\n" + "=" * 50)
    print("Test: Health check")
    print("=" * 50)
    
    url = f"{BASE_URL}/health"
    
    try:
        response = requests.get(url)
        print(f"Status Code: {response.status_code}")
        print(f"Response: {json.dumps(response.json(), indent=2)}")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    print("Iniciando tests dels endpoints...")
    
    # Test health
    test_health()
    
    # Test login valid i obtenir token
    token = test_login()
    
    # Test login amb credentials inválides
    test_login_invalid()
    
    # Test login per token (si tenim token)
    if token:
        test_login_by_token(token)
    
    # Test login per token inválid
    test_login_by_invalid_token()
    
    print("\n" + "=" * 50)
    print("Tests completats!")
    print("=" * 50)
