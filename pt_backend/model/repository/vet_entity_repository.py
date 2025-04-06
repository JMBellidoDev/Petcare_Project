import copy
from sqlalchemy.orm import Session

from model.tables.tables import VetEntity
from model.utils.data_converter import converter_cif, converter_email, converter_name
from model.utils.repository_exceptions import EntityAlreadyExistsError, EntityNotFoundError
from security.constants import SCOPE_VET_ENTITY

from passlib.context import CryptContext

# Contexto de encriptado de contraseñas
crypt_context = CryptContext(schemes = ["bcrypt"])

def find_by_id(db: Session, vet_entity_id: int) -> VetEntity:
  """
  Busca una entidad veterinaria dado el ID

  Args:
    db (Session): Sesión de la base de datos con la cual se realizarán las transacciones
    vet_entity_id (id): ID a buscar en la base de datos

  Returns:
    VetEntity: Entidad veterinaria con todos los datos en caso de ser encontrado, None en caso contrario
  """

  return db.query(VetEntity).filter(VetEntity.id == vet_entity_id).first()


def find_by_username(db: Session, vet_entity_username: str) -> VetEntity:
  """
  Busca una entidad veterinaria dado el username

  Args:
    db (Session): Sesión de la base de datos con la cual se realizarán las transacciones
    vet_entity_username (str): Username a buscar en la base de datos

  Returns:
    VetEntity: Entidad veterinaria con todos los datos en caso de ser encontrado, None en caso contrario
  """

  return db.query(VetEntity).filter(VetEntity.username == vet_entity_username).first()


def find_by_cif(db: Session, vet_entity_cif: str) -> VetEntity:
  """
  Busca un cliente dado el NIF/NIE

  Args:
    db (Session): Sesión de la base de datos con la cual se realizarán las transacciones
    vet_entity_cif (str): CIF de la entidad veterinaria

  Returns:
    VetEntity: Entidad veterinaria con todos los datos en caso de ser encontrado, None en caso contrario
  """

  return db.query(VetEntity).filter(VetEntity.cif == vet_entity_cif).first()


def create(db: Session, vet_entity: VetEntity) -> VetEntity:
  """
  Crea una entidad veterinaria en la DB

  Args:
    db (Session): Sesión de la base de datos con la cual se realizarán las transacciones
    vet_entity (VetEntity): Entidad veterinaria con todos los datos necesarios para crear el registro

  Returns:
    VetEntity: Entidad veterinaria creado con el ID generado

  Raises:
    UserAlreadyExists: En caso de que se esté intentando crear un nuevo cliente con 
  """

  # Se verifica que no existan los datos únicos en la DB
  found_vet_entity_by_cif = find_by_cif(db, vet_entity.cif)
  found_vet_entity_by_username = find_by_username(db, vet_entity.username)
  if found_vet_entity_by_cif or found_vet_entity_by_username:
    raise EntityAlreadyExistsError

  copy_vet_entity = copy.deepcopy(vet_entity)

  # Se hashea la contraseña y se asigna su role
  copy_vet_entity.hashed_password = crypt_context.encrypt(vet_entity.hashed_password)
  copy_vet_entity.role = SCOPE_VET_ENTITY

  # Se modifican los datos para su almacenamiento en la DB
  copy_vet_entity.email = converter_email(vet_entity.email)
  copy_vet_entity.name = converter_name(vet_entity.name)
  copy_vet_entity.cif = converter_cif(vet_entity.cif)

  # Se almacena el cliente
  db.add(copy_vet_entity)
  db.commit()

  db.refresh(copy_vet_entity)
  return copy_vet_entity


def update(db: Session, vet_entity: VetEntity) -> VetEntity:
  """
  Actualiza los datos de una entidad veterinaria en la DB. Los datos que se pueden actualizar son: 
    - name
    - address
    - phone_number

  Args:
    db (Session): Sesión de la base de datos con la cual se realizarán las transacciones
    client (Client): Entidad Veterinaria con todos los datos necesarios para actualizar el registro

  Returns:
    VetEntity: La entidad veterinaria actualizada

  Raises:
    EntityNotFoundError: En caso de no encontrar la entidad a actualizar
  """

  # Se obtiene el cliente de la DB y se actualizan los datos
  found_vet_entity = find_by_id(db, vet_entity.id)

  if not found_vet_entity:
    raise EntityNotFoundError

  found_vet_entity.name = converter_name(vet_entity.name)
  found_vet_entity.address = vet_entity.address
  found_vet_entity.phone_number = vet_entity.phone_number

  # Se guarda en la DB y se devuelve
  db.merge(found_vet_entity)
  db.commit()

  db.refresh(found_vet_entity)
  return found_vet_entity

