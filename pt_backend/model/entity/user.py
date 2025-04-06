from pydantic import BaseModel

class UserDto(BaseModel):
  """
  Usuario base del sistema. Se trata de un DTO, puesto que no contiene todos los datos del usuario.
   Podrá ser un veterinario, cliente del sistema o una entidad veterinaria, ya sea
  clínica u hospital veterinario

  Attributes:
    id (int): ID autogenerado de la DB para el usuario
    username (str): Nombre de usuario del sistema
    role (str): Role que posee el veterinario. Será 'client', 'vet' o 'vet_entity'
    email (str): Email del usuario
    enabled (bool): Booleano que indica si el usuario está activo actualmente
  """
  
  id: int | None = None
  username: str
  role: str | None = None
  email: str | None = None
  enabled: bool | None = None


class UserCreate(UserDto):
  """
  Usuario. Incluye, además de los datos del usuario, su contraseña hasheada

  Attributes:
  id (int): ID autogenerado de la DB para el usuario
  username (str): Nombre de usuario del sistema
  role (str): Role que posee el veterinario. Será 'client', 'vet' o 'vet_entity'
  email (str): Email del usuario
  enabled (bool): Booleano que indica si el usuario está activo actualmente
  hashed_password (str): Contraseña ya hasheada para el almacenamiento de la contraseña
  """

  hashed_password: str | None = None

  class Config:
    orm_mode = True
