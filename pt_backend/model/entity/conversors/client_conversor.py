
from model.tables import tables
from model.entity import client

def table_to_entity(table_client: tables.Client) -> client.Client:
  """
  Transforma un objeto Client de la DB en un objeto Client como entidad

  Args:
    table_client (tables.Client): Cliente de la DB

  Returns: 
    client.Client: Cliente entidad
  """

  return client.Client(
    id = table_client.id,
    username = table_client.username,
    hashed_password = table_client.hashed_password,
    email = table_client.email,
    name = table_client.name,
    role = table_client.role,
    enabled = table_client.enabled,
    national_id_document = table_client.national_id_document,
    birthdate = table_client.birthdate,
    address = table_client.address,
    phone_number = table_client.phone_number
  )

def entity_to_table(entity_client: client.Client) -> tables.Client:
  """
  Transforma un objeto Client entidad en un objeto Client de la DB

  Args:
    entity_client (client.Client): Cliente entidad

  Returns: 
    tables.Client: Cliente de la DB
  """

  return tables.Client(
    id = entity_client.id,
    username = entity_client.username,
    hashed_password = entity_client.hashed_password,
    email = entity_client.email,
    role = entity_client.role,
    enabled = entity_client.enabled,
    name = entity_client.name,
    national_id_document = entity_client.national_id_document,
    birthdate = entity_client.birthdate,
    address = entity_client.address,
    phone_number = entity_client.phone_number
  )