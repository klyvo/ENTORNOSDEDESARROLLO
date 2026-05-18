# ESPECIFICACIÓ TÈCNICA - ENDPOINTS PROTOTIP 4

## 1. Servei Login

### End-point
```
POST /login
```

### Estat
Public

### Tipus de petició
`application/json`

### Paràmetres

| Paràmetre | Tipus | Descripció |
|-----------|-------|-----------|
| username | string | username o email |
| password | string | password |

### Resposta - Usuari validat OK

**HTTP Response Code:** 200 OK

**Body:**
```json
{
  "coderesponse": "1",
  "data": {
    "email": "prova@gmail.com",
    "id": 1,
    "idrole": 1,
    "password": "12345",
    "token": "",
    "username": "mare"
  },
  "msg": "Authenticated"
}
```

### Resposta - Usuari No validat

**HTTP Response Code:** 400

**Body:**
```json
{
  "coderesponse": "0",
  "msg": "No validat"
}
```

---

## 2. Servei Login per Token

### End-point
```
POST /login/token
```

### Estat
Public

### Tipus de petició
`application/json`

### Paràmetres Header

| Paràmetre | Tipus | Descripció |
|-----------|-------|-----------|
| Authorization | string | token |

### Resposta - Usuari validat OK

**HTTP Response Code:** 200 OK

**Body:**
```json
{
  "id": 1,
  "username": "mare",
  "email": "prova@gmail.com",
  "token": "token12345",
  "idrole": "2",
  "msg": "Usuari Ok",
  "coderesponse": "1"
}
```

### Resposta - Usuari No validat

**HTTP Response Code:** 400

**Body:**
```json
{
  "coderesponse": "0",
  "msg": "No validat"
}
```

---

## Notas d'Implementació

### Versió
Prototip 4

### Framework
Flask (Python)

### Base de Dades
MySQL - Base de Dades: Tapatapp

### Taules Utilisades
- User
- RelationUserChild
- Rol

### Seguretat
- Els endpoints son públics (sense autenticació pre-requerida)
- El token es generat SHA256 basant-se en username i timestamp
- El token es emmagatzema a la base de dades

### Autenticació
Per accedir als endpoints protegits del futur, usar el token obtingut en el login inicial.

### Gestió d'Errors
- Credencials inválides retorna 400
- Errors de servidor retorna 500
- Token inválid retorna 400

---

## Flux d'Ús Típic

1. **Usuari accedeix amb credencials**
   ```
   POST /login
   ```
   Obté un token

2. **Usuari usa el token per futurs requests**
   ```
   POST /login/token
   Header: Authorization: <token>
   ```
   Valida que el token és vàlid i obté les dades de l'usuari

---

## Data de Creació
2025-05-11

## Estat
Implementat i testejat
