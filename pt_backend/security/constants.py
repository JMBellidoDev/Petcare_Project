

# openssl rand -hex 32 -> Secret key para el token JWT
SECRET_KEY = "4bd52eeaea003dffb38c4572322003b08f4a45086c02b7c68b9e5f83f9b772c8"

# Algoritmo de encriptación (Hash)
ALGORITHM = "HS256"

# Tiempo de expiración para el token
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Tiempo de expiración para el refresh token
REFRESH_TOKEN_EXPIRE_DAYS = 7

### Scopes o Roles de autorización ###

# Scope para un usuario cliente de la aplicación
SCOPE_CLIENT = "client"

# Scope para un veterinario
SCOPE_VET = "vet"

# Scope para una entidad veterinaria
SCOPE_VET_ENTITY = "vet_entity"