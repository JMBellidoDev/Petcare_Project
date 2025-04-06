import copy
from sqlalchemy.orm import Session

from model.tables.tables import Client, client_pet_table
from model.utils.data_converter import converter_name, converter_email, converter_national_id_document
from model.utils.repository_exceptions import EntityAlreadyExistsError, EntityNotFoundError
from security.constants import SCOPE_CLIENT

from passlib.context import CryptContext

# Contexto de encriptado de contraseñas
crypt_context = CryptContext(schemes = ["bcrypt"])

def find_by_id(db: Session, client_id: int) -> Client:
  """
  Busca un cliente dado el ID

  Args:
    db (Session): Sesión de la base de datos con la cual se realizarán las transacciones
    client_id (id): ID a buscar en la base de datos

  Returns:
    Client: Cliente con todos los datos en caso de ser encontrado, None en caso contrario
  """

  return db.query(Client).filter(Client.id == client_id).first()


def find_by_username(db: Session, client_username: str) -> Client:
  """
  Busca un cliente dado el username

  Args:
    db (Session): Sesión de la base de datos con la cual se realizarán las transacciones
    username (str): Username a buscar en la base de datos

  Returns:
    Client: Cliente con todos los datos en caso de ser encontrado, None en caso contrario
  """

  return db.query(Client).filter(Client.username == client_username).first()


def find_by_national_id_document(db: Session, national_id_document: str) -> Client:
  """
  Busca un cliente dado el NIF/NIE

  Args:
    db (Session): Sesión de la base de datos con la cual se realizarán las transacciones
    national_id_document (str): NIF/NIE a buscar en la base de datos

  Returns:
    Client: Cliente con todos los datos en caso de ser encontrado, None en caso contrario
  """

  return db.query(Client).filter(Client.national_id_document == national_id_document).first()


def find_by_pet_id(db: Session, pet_id: int) -> list[Client]:
  """
  Busca una lista de clientes asociados a una mascota a partir del ID de la mascota

  Args:
    db (Session): Sesión de la base de datos con la cual se realizarán las transacciones
    pet_id (int): ID de la mascota

  Returns:
    list[Client]: Lista con todos los clientes que cumplen la condición
  """

  return db.query(Client).join(client_pet_table).filter(client_pet_table.c.pet_id == pet_id).all()


def create(db: Session, client: Client) -> Client:
  """
  Crea un cliente en la DB

  Args:
    db (Session): Sesión de la base de datos con la cual se realizarán las transacciones
    client (Client): Cliente con todos los datos necesarios para crear el registro

  Returns:
    Client: Cliente creado con el ID generado

  Raises:
    EntityAlreadyExists: En caso de que se esté intentando crear un nuevo cliente ya existente
  """

  # Se verifica que no existan los datos únicos en la DB
  found_client_by_national_id_document = find_by_national_id_document(db, client.national_id_document)
  found_client_by_username = find_by_username(db, client.username)
  
  if found_client_by_national_id_document or found_client_by_username:
    raise EntityAlreadyExistsError
  
  # Se copia el cliente
  copy_client = copy.deepcopy(client)

  # Se hashea la contraseña y se asigna su role
  copy_client.hashed_password = crypt_context.encrypt(client.hashed_password)
  copy_client.role = SCOPE_CLIENT

  # Se modifican los datos para su correcto almacenamiento
  copy_client.email = converter_email(client.email)
  copy_client.name = converter_name(client.name)
  copy_client.national_id_document = converter_national_id_document(client.national_id_document)

  # Se almacena el cliente
  db.add(copy_client)
  db.commit()

  db.refresh(copy_client)
  return copy_client


def update(db: Session, client: Client) -> Client:
  """
  Actualiza los datos de un cliente en la DB. Los datos que se pueden actualizar son: 
    - name, 
    - birthdate
    - address
    - phone number

  Args:
    db (Session): Sesión de la base de datos con la cual se realizarán las transacciones
    client (Client): Cliente con todos los datos necesarios para actualizar el registro

  Returns:
    Client: El cliente actualizado

  Raises:
    EntityNotFoundError: En caso de no encontrar la entidad a actualizar
  """

  # Se obtiene el cliente de la DB y se actualizan los datos
  found_client = find_by_id(db, client.id)

  if not found_client:
    raise EntityNotFoundError

  found_client.name = converter_name(client.name)
  found_client.birthdate = client.birthdate
  found_client.address = client.address
  found_client.phone_number = client.phone_number

  # Se guarda en la DB y se devuelve
  db.merge(found_client)
  db.commit()

  db.refresh(found_client)
  return found_client

