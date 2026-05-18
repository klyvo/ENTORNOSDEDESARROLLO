# Prototipo 4 - WebService de Login amb Flask

## Descripció

Prototip 4 implementa un webservice RESTful amb Flask que proporciona autenticació d'usuaris:
- **Login amb credencials** (username/email + password)
- **Validació per token**

## Estructura de Carpetes

```
prototipo4/
├── server/
│   ├── DaoLogin.py       # DAO per accés a la BBDD
│   └── server.py         # Servidor Flask amb endpoints
└── client/
    └── client_test.py    # Client de test dels endpoints
```

## Requisits

- Python 3.x
- Flask: `pip install Flask`
- MySQL Connector: `pip install mysql-connector-python`
- requests (per tests): `pip install requests`

## Configuració de la Base de Dades

Assegurar-se que:
1. MySQL està executant-se a `localhost:3306`
2. Existeix la base de dades `Tapatapp`
3. Existeix l'usuari `root` amb contrasenya `root`
4. Les taules User, Rol, i RelationUserChild estan creades

Usuaris de prova:
- **Username:** mare / **Password:** mare / **Email:** prova@gmail.com
- **Username:** pare / **Password:** pare / **Email:** prova2@gmail.com

## Com Executar

### 1. Iniciar el Servidor Flask

```bash
cd prototipo4/server
python server.py
```

El servidor escoltarà a `http://localhost:5000`

### 2. Executar els Tests (en altre terminal)

```bash
cd prototipo4/client
python client_test.py
```

## Endpoints

### 1. Login amb Credencials

**Endpoint:** `POST /login`

**Content-Type:** `application/json`

**Paràmetres (body):**
```json
{
  "username": "mare",
  "password": "mare"
}
```

**Resposta Exitosa (200 OK):**
```json
{
  "coderesponse": "1",
  "data": {
    "email": "prova@gmail.com",
    "id": 1,
    "idrole": 1,
    "password": "mare",
    "token": "abc123...",
    "username": "mare"
  },
  "msg": "Authenticated"
}
```

**Resposta Error (400):**
```json
{
  "coderesponse": "0",
  "msg": "No validat"
}
```

### 2. Login per Token

**Endpoint:** `POST /login/token`

**Headers:**
```
Authorization: abc123...
Content-Type: application/json
```

**Paràmetres:** Sense cos (body buit)

**Resposta Exitosa (200 OK):**
```json
{
  "id": 1,
  "username": "mare",
  "email": "prova@gmail.com",
  "token": "abc123...",
  "idrole": "1",
  "msg": "Usuari Ok",
  "coderesponse": "1"
}
```

**Resposta Error (400):**
```json
{
  "coderesponse": "0",
  "msg": "No validat"
}
```

### 3. Health Check

**Endpoint:** `GET /health`

**Resposta:**
```json
{
  "status": "ok"
}
```

## Exemples d'Ús amb cURL

### Login
```bash
curl -X POST http://localhost:5000/login \
  -H "Content-Type: application/json" \
  -d '{"username": "mare", "password": "mare"}'
```

### Login per Token
```bash
curl -X POST http://localhost:5000/login/token \
  -H "Authorization: <TOKEN_AQUI>" \
  -H "Content-Type: application/json"
```

### Health Check
```bash
curl http://localhost:5000/health
```

## Estructura de Dades Retornats

### Camps de l'Usuari

| Camp | Tipus | Descripció |
|------|-------|-----------|
| id | int | ID únic de l'usuari |
| username | string | Nom d'usuari |
| email | string | Email de l'usuari |
| password | string | Contrasenya (hasheada a la BBDD) |
| token | string | Token de sesió |
| idrole | int/string | ID del rol de l'usuari |

## Seguretat

**Nota:** En producció s'hauria de:
- Usar HTTPS en lloc de HTTP
- Hashejar les contrasenyes (SHA256, bcrypt, etc.)
- Implementar rate limiting
- Usar variables d'entorn per les credencials de la BBDD
- Implementar refresh tokens i expiració de tokens
- Usar prepared statements (ja implementat)

## Troubleshooting

**Error: "No module named 'mysql.connector'"**
```bash
pip install mysql-connector-python
```

**Error: "Connection refused"**
- Verificar que MySQL està executant-se
- Verificar les credencials de la BBDD en DaoLogin.py

**Error: "Unknown database"**
- Verificar que la BBDD `Tapatapp` existeix
- Executar el script SQL d'inicialització

## Autor

Desenvolupat com a Prototip 4 del projecte Tapatapp
