from sqlalchemy.orm import Session

from model.tables.tables import User
from model.entity.user import UserDto, UserCreate
from model.entity.conversors.user_conversor import create_entity_to_table

from passlib.context import CryptContext

# Contexto de encriptado de contraseñas
crypt_context = CryptContext(schemes = ["bcrypt"])

def find_by_id(db: Session, user_id: int) -> UserDto:
  """
  Busca un usuario dado el ID

  Args:
    db (Session): Sesión de la base de datos con la cual se realizarán las transacciones
    user_id (id): ID a buscar en la base de datos

  Returns:
    User: Usuario con todos los datos en caso de ser encontrado, None en caso contrario
  """

  return db.query(User).filter(User.id == user_id).first()

  

def find_by_username(db: Session, username: str) -> UserCreate:
  """
  Busca un usuario dado el username

  Args:
    db (Session): Sesión de la base de datos con la cual se realizarán las transacciones
    username (str): Username a buscar en la base de datos

  Returns:
    User: Usuario con todos los datos en caso de ser encontrado, None en caso contrario
  """

  return db.query(User).filter(User.username == username).first()


def enable_disable(db: Session, user_id: int, enabled: bool):
  """
  Habilita o deshabilita un usuario del sistema para permitir su acceso mediante el login

  Args:
    db (Session): Sesión de la base de datos con la cual se realizarán las transacciones
    user_id (id): ID del usuario
    enabled (bool): Indica si el usuario se va a habilitar o deshabilitar

  Returns:
    None
  """

  user = find_by_id(db, user_id)

  if user:
    user.enabled = enabled
    db.merge(user)
    db.commit()