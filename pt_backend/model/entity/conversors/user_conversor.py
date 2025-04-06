
from model.entity import user
from model.tables import tables

def table_to_entity_dto(table_user: tables.User) -> user.UserDto:
  """
  Transforma un objeto User de la DB en un objeto UserDto como entidad

  Args:
    table_user (tables.User): Usuario de la DB

  Returns: 
    user.UserDto: Usuario entidad DTO
  """

  return user.UserDto(
    id = table_user.id,
    username = table_user.username,
    email = table_user.email,
    role = table_user.role,
    enabled = table_user.enabled,
  )

def dto_entity_to_table(user_dto: user.UserDto) -> tables.User:
  """
  Transforma un objeto UserDto en un objeto User de la DB

  Args:
    user_dto (user.UserDto): Usuario entidad DTO

  Returns: 
    tables.User: Usuario de la DB
  """

  return tables.User(
    id = user_dto.id,
    username = user_dto.username,
    email = user_dto.email,
    role = user_dto.role,
    enabled = user_dto.enabled,
  )

def table_to_entity_create(table_user: tables.User) -> user.UserCreate:
  """
  Transforma un objeto User de la DB en un objeto UserCreate como entidad

  Args:
    table_user (tables.User): Usuario de la DB

  Returns: 
    user.UserCreate: Usuario entidad de creación
  """

  return user.UserCreate(
    id = table_user.id,
    username = table_user.username,
    email = table_user.email,
    role = table_user.role,
    enabled = table_user.enabled,
    hashed_password = table_user.hashed_password
  )

def create_entity_to_table(user_create: user.UserCreate) -> tables.User:
  """
  Transforma un objeto UserCreate en un objeto User de la DB

  Args:
    user_dto (user.UserCreate): Usuario entidad de creación

  Returns: 
    tables.User: Usuario de la DB
  """

  return tables.User(
    id = user_create.id,
    username = user_create.username,
    email = user_create.email,
    role = user_create.role,
    enabled = user_create.enabled,
    hashed_password = user_create.hashed_password
  )