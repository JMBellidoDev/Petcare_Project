import copy
from sqlalchemy.orm import Session, joinedload

from model.tables.tables import Vet, VetEntity
from model.utils.data_converter import converter_name, converter_email, converter_national_id_document
from model.utils.repository_exceptions import EntityAlreadyExistsError, EntityNotFoundError
from security.constants import SCOPE_VET

from passlib.context import CryptContext

# Contexto de encriptado de contraseñas
crypt_context = CryptContext(schemes = ["bcrypt"])

def find_by_id(db: Session, vet_id: int) -> Vet:
  """
  Busca un veterinario dado el ID

  Args:
    db (Session): Sesión de la base de datos con la cual se realizarán las transacciones
    vet_id (id): ID a buscar en la base de datos

  Returns:
    Vet: Veterinario con todos los datos en caso de ser encontrado, None en caso contrario
  """

  return (db.query(Vet)
          .options(joinedload(Vet.vet_entity).load_only(VetEntity.id, VetEntity.name))
          .filter(Vet.id == vet_id)
          .first())


def find_by_username(db: Session, vet_username: str) -> Vet:
  """
  Busca un veterinario dado el username

  Args:
    db (Session): Sesión de la base de datos con la cual se realizarán las transacciones
    vet_username (str): Username a buscar en la base de datos

  Returns:
    Vet: Veterinario con todos los datos en caso de ser encontrado, None en caso contrario
  """

  return (db.query(Vet)
          .options(joinedload(Vet.vet_entity).load_only(VetEntity.id, VetEntity.name))
          .filter(Vet.username == vet_username)
          .first())


def find_by_national_id_document(db: Session, national_id_document: str) -> Vet:
  """
  Busca un veterinario dado el NIF/NIE

  Args:
    db (Session): Sesión de la base de datos con la cual se realizarán las transacciones
    national_id_document (str): NIF/NIE a buscar en la base de datos

  Returns:
    Vet: Veterinario con todos los datos en caso de ser encontrado, None en caso contrario
  """

  return (db.query(Vet)
          .options(joinedload(Vet.vet_entity).load_only(VetEntity.id, VetEntity.name))
          .filter(Vet.national_id_document == national_id_document)
          .first())


def find_by_vet_entity_id(db: Session, vet_entity_id: int) -> list[Vet]:
  """
  Busca todos los veterinarios asociados a una entidad concreta

  Args:
    db (Session): Sesión de la base de datos con la cual se realizarán las transacciones
    vet_entity_id (int): ID de la entidad veterinaria

  Returns:
    list[Vet]: Lista con todos los veterinarios que cumplen la condición
  """

  return (db.query(Vet)
          .options(joinedload(Vet.vet_entity).load_only(VetEntity.id, VetEntity.name))
          .filter(Vet.vet_entity_id == vet_entity_id)
          .all())


def create(db: Session, vet: Vet) -> Vet:
  """
  Crea un veterinario en la DB

  Args:
    db (Session): Sesión de la base de datos con la cual se realizarán las transacciones
    vet (Vet): Veterinario con todos los datos necesarios para crear el registro

  Returns:
    Vet: Veterinario creado con el ID generado

  Raises:
    EntityAlreadyExists: En caso de que se esté intentando crear un nuevo cliente ya existente
  """

  # Se verifica que no existan los datos únicos en la DB
  found_vet_by_national_id_document = find_by_national_id_document(db, vet.national_id_document)
  found_vet_by_username = find_by_username(db, vet.username)
  if found_vet_by_national_id_document or found_vet_by_username:
    raise EntityAlreadyExistsError

  # Se copia el veterinario
  copy_vet = copy.deepcopy(vet)

  # Se hashea la contraseña y se asigna su role
  copy_vet.hashed_password = crypt_context.encrypt(vet.hashed_password)
  copy_vet.role = SCOPE_VET

  # Se transforman los datos
  copy_vet.email = converter_email(vet.email)
  copy_vet.name = converter_email(vet.name)
  copy_vet.national_id_document = converter_national_id_document(vet.national_id_document)

  # Se almacena el cliente

  db.add(copy_vet)
  db.commit()

  db.refresh(copy_vet)
  return copy_vet


def update(db: Session, vet: Vet) -> Vet:
  """
  Actualiza los datos de un veterinario en la DB. Los datos que se pueden actualizar son: 
    - name

  Args:
    db (Session): Sesión de la base de datos con la cual se realizarán las transacciones
    vet (Vet): Veterinario con todos los datos necesarios para actualizar el registro

  Returns:
    Vet: El veterinario actualizado

  Raises:
    EntityNotFoundError: En caso de no encontrar la entidad a actualizar
  """

  # Se obtiene el cliente de la DB y se actualizan los datos
  found_vet = find_by_id(db, vet.id)

  if not found_vet:
    raise EntityNotFoundError

  found_vet.name = converter_name(vet.name)
  found_vet.enabled = vet.enabled
  found_vet.vet_entity_id = vet.vet_entity_id

  # Se guarda en la DB y se devuelve
  db.merge(found_vet)
  db.commit()

  db.refresh(found_vet)
  return found_vet

