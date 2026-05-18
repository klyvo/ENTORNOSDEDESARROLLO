"""
EXEMPLOS D'ÚS DELS ENDPOINTS - HTTP Requests

Aquests són exemples de crides HTTP que pots fazer als endpoints
Pots usar postman, curl, o qualsevol client HTTP

BASE URL: http://localhost:5000
"""

# ============================================================================
# 1. LOGIN AMB CREDENCIALS
# ============================================================================

# Endpoint: POST /login
# Headers: Content-Type: application/json

REQUEST_LOGIN = {
    "method": "POST",
    "url": "http://localhost:5000/login",
    "headers": {
        "Content-Type": "application/json"
    },
    "body": {
        "username": "mare",
        "password": "mare"
    }
}

# Response (200 OK):
RESPONSE_LOGIN_SUCCESS = {
    "coderesponse": "1",
    "data": {
        "email": "prova@gmail.com",
        "id": 1,
        "idrole": 1,
        "password": "mare",
        "token": "8f8e8b7c6d5e4f3a2b1c0d9e8f7a6b5c4d3e2f1a0b9c8d7e6f5a4b3c2d1e0f",
        "username": "mare"
    },
    "msg": "Authenticated"
}

# Response (400 Error):
RESPONSE_LOGIN_ERROR = {
    "coderesponse": "0",
    "msg": "No validat"
}


# ============================================================================
# 2. LOGIN PER TOKEN
# ============================================================================

# Endpoint: POST /login/token
# Headers: Authorization: <token>, Content-Type: application/json
# Body: (buit)

REQUEST_LOGIN_TOKEN = {
    "method": "POST",
    "url": "http://localhost:5000/login/token",
    "headers": {
        "Content-Type": "application/json",
        "Authorization": "8f8e8b7c6d5e4f3a2b1c0d9e8f7a6b5c4d3e2f1a0b9c8d7e6f5a4b3c2d1e0f"
    },
    "body": {}
}

# Response (200 OK):
RESPONSE_LOGIN_TOKEN_SUCCESS = {
    "id": 1,
    "username": "mare",
    "email": "prova@gmail.com",
    "token": "8f8e8b7c6d5e4f3a2b1c0d9e8f7a6b5c4d3e2f1a0b9c8d7e6f5a4b3c2d1e0f",
    "idrole": "1",
    "msg": "Usuari Ok",
    "coderesponse": "1"
}

# Response (400 Error):
RESPONSE_LOGIN_TOKEN_ERROR = {
    "coderesponse": "0",
    "msg": "No validat"
}


# ============================================================================
# 3. HEALTH CHECK
# ============================================================================

# Endpoint: GET /health
# Headers: (cap)
# Body: (buit)

REQUEST_HEALTH = {
    "method": "GET",
    "url": "http://localhost:5000/health",
    "headers": {},
    "body": {}
}

# Response (200 OK):
RESPONSE_HEALTH = {
    "status": "ok"
}


# ============================================================================
# EXEMPLES CURL
# ============================================================================

"""
# 1. Login
curl -X POST http://localhost:5000/login \\
  -H "Content-Type: application/json" \\
  -d '{"username": "mare", "password": "mare"}'


# 2. Login per Token (substituir TOKEN_AQUI per un token vàlid)
curl -X POST http://localhost:5000/login/token \\
  -H "Content-Type: application/json" \\
  -H "Authorization: TOKEN_AQUI"


# 3. Health Check
curl -X GET http://localhost:5000/health


# 4. Login amb email en lugar de username
curl -X POST http://localhost:5000/login \\
  -H "Content-Type: application/json" \\
  -d '{"username": "prova@gmail.com", "password": "mare"}'
"""


# ============================================================================
# EXEMPLES Python (usando requests)
# ============================================================================

"""
import requests
import json

# Login
url = "http://localhost:5000/login"
headers = {"Content-Type": "application/json"}
data = {"username": "mare", "password": "mare"}
response = requests.post(url, json=data, headers=headers)
print(response.status_code)
print(response.json())

# Login per Token
url = "http://localhost:5000/login/token"
headers = {
    "Content-Type": "application/json",
    "Authorization": "TOKEN_AQUI"
}
response = requests.post(url, headers=headers)
print(response.status_code)
print(response.json())

# Health Check
url = "http://localhost:5000/health"
response = requests.get(url)
print(response.status_code)
print(response.json())
"""


# ============================================================================
# EXEMPLES JavaScript (usando fetch)
# ============================================================================

"""
// Login
fetch('http://localhost:5000/login', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
    username: 'mare',
    password: 'mare'
  })
})
.then(response => response.json())
.then(data => console.log(data))
.catch(error => console.error('Error:', error));


// Login per Token
fetch('http://localhost:5000/login/token', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
    'Authorization': 'TOKEN_AQUI'
  }
})
.then(response => response.json())
.then(data => console.log(data))
.catch(error => console.error('Error:', error));


// Health Check
fetch('http://localhost:5000/health')
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error('Error:', error));
"""
